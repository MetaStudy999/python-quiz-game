import json
import os
import random
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from quiz import Quiz


DEFAULT_QUIZ_DATA = [
    {
        "question": "Python에서 문자열을 이어 붙일 때 사용하는 연산자는 무엇인가요?",
        "choices": ["+", "-", "*", "/"],
        "answer": 1,
        "hint": "문자열 결합은 덧셈 기호를 사용합니다.",
    },
    {
        "question": "다음 중 리스트를 나타내는 자료형 표기는 무엇인가요?",
        "choices": ["{}", "()", "[]", "<>"],
        "answer": 3,
        "hint": "리스트는 대괄호를 사용합니다.",
    },
    {
        "question": "조건이 참일 때만 코드를 실행하도록 만드는 문장은 무엇인가요?",
        "choices": ["for", "if", "while", "def"],
        "answer": 2,
        "hint": "영어로 '만약'이라는 뜻의 키워드입니다.",
    },
    {
        "question": "Git에서 작업 내역을 저장하는 기록 단위를 무엇이라고 하나요?",
        "choices": ["clone", "branch", "commit", "pull"],
        "answer": 3,
        "hint": "변경 이력을 남길 때 사용하는 명령어 이름과 같습니다.",
    },
    {
        "question": "원격 저장소의 변경 사항을 내 컴퓨터로 가져오는 Git 명령어는 무엇인가요?",
        "choices": ["push", "merge", "checkout", "pull"],
        "answer": 4,
        "hint": "밀어 넣는(push)의 반대 방향으로 생각해 보세요.",
    },
    {
        "question": "함수를 정의할 때 사용하는 Python 키워드는 무엇인가요?",
        "choices": ["class", "return", "def", "import"],
        "answer": 3,
        "hint": "define의 앞부분을 줄여 쓴 형태입니다.",
    },
]


class SafeExitRequested(Exception):
    pass


class QuizGame:
    def __init__(self, state_path: Optional[Path] = None) -> None:
        self.state_path = state_path or Path(__file__).resolve().parent / "state.json"
        self.quizzes: list[Quiz] = []
        self.best_score: Optional[dict] = None
        self.score_history: list[dict] = []
        self.startup_message = ""
        self.startup_message_level = "info"
        self.use_color = self._supports_color()
        self._load_state()

    def run(self) -> None:
        self._print_title()
        if self.startup_message:
            print(self._status_text(self.startup_message, level=self.startup_message_level))
            print("=" * 40)

        try:
            while True:
                self._print_menu()
                selected_menu = self._prompt_number("선택: ", 1, 6)
                print()

                if selected_menu == 1:
                    self.play_quiz()
                elif selected_menu == 2:
                    self.add_quiz()
                elif selected_menu == 3:
                    self.show_quiz_list()
                elif selected_menu == 4:
                    self.show_best_score()
                elif selected_menu == 5:
                    self.delete_quiz()
                else:
                    self._save_state()
                    print(self._info_text("프로그램을 종료합니다. 데이터를 저장했습니다.", "💾"))
                    return
        except SafeExitRequested:
            print()
            print(self._warning_text("입력이 중단되어 현재 데이터를 저장한 뒤 종료합니다."))
            self._save_state()

    def _print_title(self) -> None:
        line = self._style("=" * 40, color="36", bold=True)
        print(line)
        print(self._style("      🎯 나만의 퀴즈 게임 🎯", color="35", bold=True))
        print(line)

    def _print_menu(self) -> None:
        print(self._style("1. 📝 퀴즈 풀기", color="36"))
        print(self._style("2. ➕ 퀴즈 추가", color="32"))
        print(self._style("3. 📋 퀴즈 목록", color="34"))
        print(self._style("4. 🏆 점수 확인", color="33"))
        print(self._style("5. 🗑️ 퀴즈 삭제", color="31"))
        print(self._style("6. 👋 종료", color="35"))
        print(self._style("=" * 40, color="36", bold=True))

    def _prompt_text(self, message: str) -> str:
        while True:
            raw_value = self._safe_input(message).strip()

            if raw_value:
                return raw_value

            print(self._warning_text("입력이 비어 있습니다. 다시 입력해 주세요."))

    def _prompt_number(self, message: str, minimum: int, maximum: int) -> int:
        while True:
            raw_value = self._safe_input(message).strip()

            if not raw_value:
                print(self._warning_text("입력이 비어 있습니다. 다시 입력해 주세요."))
                continue

            try:
                number = int(raw_value)
            except ValueError:
                print(self._warning_text(f"잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요."))
                continue

            if number < minimum or number > maximum:
                print(self._warning_text(f"허용 범위를 벗어났습니다. {minimum}-{maximum} 사이의 숫자를 입력하세요."))
                continue

            return number

    def _safe_input(self, message: str) -> str:
        try:
            return input(message)
        except (EOFError, KeyboardInterrupt) as error:
            raise SafeExitRequested from error

    def play_quiz(self) -> None:
        if not self.quizzes:
            print(self._warning_text("등록된 퀴즈가 없어 게임을 시작할 수 없습니다."))
            print()
            return

        question_count = self._select_question_count()
        selected_quizzes = random.sample(self.quizzes, k=question_count)
        total_questions = len(selected_quizzes)
        correct_count = 0
        hints_used = 0

        print(self._info_text(f"퀴즈를 시작합니다! (총 {total_questions}문제, 랜덤 출제)", "📝"))
        print()

        for index, quiz in enumerate(selected_quizzes, start=1):
            quiz.display(index)
            selected_answer, used_hint = self._prompt_answer_with_hint(quiz)
            if used_hint:
                hints_used += 1

            if quiz.is_correct(selected_answer):
                correct_count += 1
                print(self._success_text("정답입니다!"))
            else:
                print(self._error_text(f"오답입니다. 정답은 {quiz.answer}번입니다."))

            print()

        hint_penalty = hints_used * 10
        points = max(0, int((correct_count / total_questions) * 100) - hint_penalty)
        result = {
            "points": points,
            "correct_count": correct_count,
            "total_questions": total_questions,
            "hints_used": hints_used,
        }
        self._append_score_history(result)

        print(self._style("=" * 40, color="36", bold=True))
        print(self._highlight_text(f"결과: {total_questions}문제 중 {correct_count}문제 정답! ({points}점)", "🎯"))
        if hints_used:
            print(self._hint_text(f"힌트 사용: {hints_used}회 (-{hint_penalty}점)"))

        if self._is_new_best_score(result):
            self.best_score = result
            print(self._score_text("새로운 최고 점수입니다!", "🎉"))
        else:
            print(self._score_text("최고 점수는 유지되었습니다.", "🏆"))

        self._save_state()
        print(self._style("=" * 40, color="36", bold=True))
        print()

    def _select_question_count(self) -> int:
        available_count = len(self.quizzes)

        if available_count == 1:
            return 1

        print(self._info_text(f"현재 등록된 퀴즈는 총 {available_count}개입니다.", "📚"))
        return self._prompt_number(
            f"이번에 풀 문제 수를 선택하세요 (1-{available_count}): ",
            1,
            available_count,
        )

    def add_quiz(self) -> None:
        print(self._info_text("새로운 퀴즈를 추가합니다.", "➕"))
        question = self._prompt_text("문제를 입력하세요: ")
        choices = []

        for index in range(1, 5):
            choice = self._prompt_text(f"선택지 {index}: ")
            choices.append(choice)

        hint = self._safe_input("힌트 (선택 입력, Enter로 건너뛰기): ").strip()
        answer = self._prompt_number("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer, hint))
        self._save_state()
        print(self._success_text("퀴즈가 추가되었습니다!"))
        print()

    def show_quiz_list(self) -> None:
        if not self.quizzes:
            print(self._warning_text("등록된 퀴즈가 없습니다."))
            print()
            return

        print(self._info_text(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)", "📋"))
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("-" * 40)
        print()

    def show_best_score(self) -> None:
        if not self.best_score:
            print(self._warning_text("아직 저장된 최고 점수가 없습니다. 먼저 퀴즈를 풀어 보세요."))
            print()
            return

        score_text = self._format_score(self.best_score)
        print(self._score_text(f"최고 점수: {score_text}"))
        if self.score_history:
            print(self._info_text("최근 기록:", "🕘"))
            for record in self.score_history[-5:]:
                print(f"- {self._format_history_record(record)}")
        print()

    def delete_quiz(self) -> None:
        if not self.quizzes:
            print(self._warning_text("삭제할 퀴즈가 없습니다."))
            print()
            return

        print(self._info_text(f"삭제할 퀴즈를 선택하세요. (총 {len(self.quizzes)}개)", "🗑️"))
        print("-" * 40)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("-" * 40)

        selected_index = self._prompt_number(
            f"삭제할 번호를 입력하세요 (취소는 0, 0-{len(self.quizzes)}): ",
            0,
            len(self.quizzes),
        )

        if selected_index == 0:
            print(self._info_text("퀴즈 삭제를 취소했습니다.", "↩️"))
            print()
            return

        deleted_quiz = self.quizzes.pop(selected_index - 1)
        self._save_state()
        print(self._success_text(f"삭제되었습니다: {deleted_quiz.question}", icon="🗑️"))
        print()

    def _load_state(self) -> None:
        if not self.state_path.exists():
            self.quizzes = self._default_quizzes()
            self.best_score = None
            self.startup_message = (
                "state.json이 없어 기본 퀴즈 데이터로 새로 시작합니다."
            )
            self.startup_message_level = "info"
            self._save_state()
            return

        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                raw_state = json.load(file)

            if not isinstance(raw_state, dict):
                raise ValueError("state.json 최상위 구조는 객체여야 합니다.")

            if "quizzes" not in raw_state or "best_score" not in raw_state:
                raise ValueError("state.json 필수 키가 누락되었습니다.")

            self.quizzes = self._load_quizzes(raw_state.get("quizzes", []))
            self.best_score = self._load_best_score(raw_state.get("best_score"))
            self.score_history = self._load_score_history(
                raw_state.get("score_history", [])
            )
            self.startup_message = self._build_loaded_message()
            self.startup_message_level = "info"
        except (OSError, json.JSONDecodeError, ValueError, TypeError):
            self.quizzes = self._default_quizzes()
            self.best_score = None
            self.score_history = []
            self.startup_message = (
                "state.json이 손상되었거나 읽을 수 없어 기본 데이터로 복구했습니다."
            )
            self.startup_message_level = "warning"
            self._save_state()

    def _save_state(self) -> None:
        state = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "score_history": self.score_history,
        }

        try:
            with self.state_path.open("w", encoding="utf-8") as file:
                json.dump(state, file, ensure_ascii=False, indent=4)
        except OSError:
            print(self._error_text("파일 저장 중 문제가 발생했습니다. 권한과 경로를 확인해 주세요."))

    def _default_quizzes(self) -> list[Quiz]:
        return [Quiz.from_dict(quiz_data) for quiz_data in DEFAULT_QUIZ_DATA]

    def _load_quizzes(self, raw_quizzes: list[dict]) -> list[Quiz]:
        if not isinstance(raw_quizzes, list):
            raise ValueError("quizzes 데이터는 리스트여야 합니다.")

        quizzes = []
        for raw_quiz in raw_quizzes:
            quizzes.append(Quiz.from_dict(raw_quiz))

        return quizzes

    def _prompt_answer_with_hint(self, quiz: Quiz) -> tuple[int, bool]:
        hint_was_used = False

        while True:
            if quiz.has_hint():
                raw_value = self._safe_input("정답 입력 (1-4, 힌트는 h): ").strip()
            else:
                raw_value = self._safe_input("정답 입력 (1-4): ").strip()

            if not raw_value:
                print(self._warning_text("입력이 비어 있습니다. 다시 입력해 주세요."))
                continue

            if quiz.has_hint() and raw_value.lower() == "h":
                print(self._hint_text(f"힌트: {quiz.hint}"))
                hint_was_used = True
                continue

            try:
                selected_answer = int(raw_value)
            except ValueError:
                if quiz.has_hint():
                    print(self._warning_text("잘못된 입력입니다. 1-4 또는 h를 입력하세요."))
                else:
                    print(self._warning_text("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요."))
                continue

            if selected_answer < 1 or selected_answer > 4:
                print(self._warning_text("허용 범위를 벗어났습니다. 1-4 사이의 숫자를 입력하세요."))
                continue

            return selected_answer, hint_was_used

    def _append_score_history(self, result: dict) -> None:
        history_record = {
            "played_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": result["total_questions"],
            "correct_count": result["correct_count"],
            "points": result["points"],
            "hints_used": result.get("hints_used", 0),
        }
        self.score_history.append(history_record)

    def _load_score_history(self, raw_history: list[dict]) -> list[dict]:
        if not isinstance(raw_history, list):
            raise ValueError("score_history 데이터는 리스트여야 합니다.")

        history = []
        for raw_record in raw_history:
            if not isinstance(raw_record, dict):
                raise ValueError("점수 기록 형식이 올바르지 않습니다.")

            history.append(
                {
                    "played_at": str(raw_record.get("played_at", "")),
                    "total_questions": int(raw_record.get("total_questions", 0)),
                    "correct_count": int(raw_record.get("correct_count", 0)),
                    "points": int(raw_record.get("points", 0)),
                    "hints_used": int(raw_record.get("hints_used", 0)),
                }
            )

        return history

    def _load_best_score(self, raw_best_score: Optional[dict]) -> Optional[dict]:
        if raw_best_score is None:
            return None

        if isinstance(raw_best_score, int):
            return {
                "points": raw_best_score,
                "correct_count": 0,
                "total_questions": 0,
            }

        if not isinstance(raw_best_score, dict):
            raise ValueError("best_score 데이터 형식이 올바르지 않습니다.")

        points = int(raw_best_score.get("points", 0))
        correct_count = int(raw_best_score.get("correct_count", 0))
        total_questions = int(raw_best_score.get("total_questions", 0))

        if points < 0 or correct_count < 0 or total_questions < 0:
            raise ValueError("best_score에는 음수를 저장할 수 없습니다.")

        if total_questions and correct_count > total_questions:
            raise ValueError("정답 수는 전체 문제 수보다 클 수 없습니다.")

        return {
            "points": points,
            "correct_count": correct_count,
            "total_questions": total_questions,
        }

    def _is_new_best_score(self, result: dict) -> bool:
        if not self.best_score:
            return True

        current_points = self.best_score["points"]
        new_points = result["points"]

        if new_points > current_points:
            return True

        if new_points == current_points:
            return result["correct_count"] > self.best_score["correct_count"]

        return False

    def _build_loaded_message(self) -> str:
        if self.best_score:
            best_score_text = f"{self.best_score['points']}점"
        else:
            best_score_text = "기록 없음"

        return (
            f"저장된 데이터를 불러왔습니다. "
            f"(퀴즈 {len(self.quizzes)}개, 최고 점수 {best_score_text}, 기록 {len(self.score_history)}개)"
        )

    def _format_score(self, score: dict) -> str:
        if score["total_questions"] == 0:
            return f"{score['points']}점"

        return (
            f"{score['points']}점 "
            f"({score['total_questions']}문제 중 {score['correct_count']}문제 정답)"
        )

    def _format_history_record(self, record: dict) -> str:
        history_text = (
            f"{record['played_at']} | "
            f"{record['total_questions']}문제 중 {record['correct_count']}문제 정답 | "
            f"{record['points']}점"
        )

        if record.get("hints_used", 0):
            history_text += f" | 힌트 {record['hints_used']}회"

        return history_text

    def _supports_color(self) -> bool:
        return sys.stdout.isatty() and os.getenv("TERM", "").lower() != "dumb"

    def _style(self, text: str, color: Optional[str] = None, bold: bool = False) -> str:
        if not self.use_color:
            return text

        codes = []
        if bold:
            codes.append("1")
        if color:
            codes.append(color)

        if not codes:
            return text

        return f"\033[{';'.join(codes)}m{text}\033[0m"

    def _status_text(self, text: str, level: str = "info") -> str:
        if level == "warning":
            return self._warning_text(text)
        if level == "error":
            return self._error_text(text)
        return self._info_text(text, "📂")

    def _info_text(self, text: str, icon: str = "ℹ️") -> str:
        return self._style(f"{icon} {text}", color="36", bold=True)

    def _warning_text(self, text: str) -> str:
        return self._style(f"⚠️ {text}", color="33", bold=True)

    def _success_text(self, text: str, icon: str = "✅") -> str:
        return self._style(f"{icon} {text}", color="32", bold=True)

    def _error_text(self, text: str) -> str:
        return self._style(f"❌ {text}", color="31", bold=True)

    def _hint_text(self, text: str) -> str:
        return self._style(f"💡 {text}", color="36", bold=True)

    def _score_text(self, text: str, icon: str = "🏆") -> str:
        return self._style(f"{icon} {text}", color="33", bold=True)

    def _highlight_text(self, text: str, icon: str = "🎯") -> str:
        return self._style(f"{icon} {text}", color="35", bold=True)
