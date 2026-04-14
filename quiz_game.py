import json
import random
from pathlib import Path
from typing import Optional

from quiz import Quiz


DEFAULT_QUIZ_DATA = [
    {
        "question": "Python에서 문자열을 이어 붙일 때 사용하는 연산자는 무엇인가요?",
        "choices": ["+", "-", "*", "/"],
        "answer": 1,
    },
    {
        "question": "다음 중 리스트를 나타내는 자료형 표기는 무엇인가요?",
        "choices": ["{}", "()", "[]", "<>"],
        "answer": 3,
    },
    {
        "question": "조건이 참일 때만 코드를 실행하도록 만드는 문장은 무엇인가요?",
        "choices": ["for", "if", "while", "def"],
        "answer": 2,
    },
    {
        "question": "Git에서 작업 내역을 저장하는 기록 단위를 무엇이라고 하나요?",
        "choices": ["clone", "branch", "commit", "pull"],
        "answer": 3,
    },
    {
        "question": "원격 저장소의 변경 사항을 내 컴퓨터로 가져오는 Git 명령어는 무엇인가요?",
        "choices": ["push", "merge", "checkout", "pull"],
        "answer": 4,
    },
    {
        "question": "함수를 정의할 때 사용하는 Python 키워드는 무엇인가요?",
        "choices": ["class", "return", "def", "import"],
        "answer": 3,
    },
]


class SafeExitRequested(Exception):
    pass


class QuizGame:
    def __init__(self, state_path: Optional[Path] = None) -> None:
        self.state_path = state_path or Path(__file__).resolve().parent / "state.json"
        self.quizzes: list[Quiz] = []
        self.best_score: Optional[dict] = None
        self.startup_message = ""
        self._load_state()

    def run(self) -> None:
        self._print_title()
        if self.startup_message:
            print(self.startup_message)
            print("=" * 40)

        try:
            while True:
                self._print_menu()
                selected_menu = self._prompt_number("선택: ", 1, 5)
                print()

                if selected_menu == 1:
                    self.play_quiz()
                elif selected_menu == 2:
                    self.add_quiz()
                elif selected_menu == 3:
                    self.show_quiz_list()
                elif selected_menu == 4:
                    self.show_best_score()
                else:
                    self._save_state()
                    print("프로그램을 종료합니다. 데이터를 저장했습니다.")
                    return
        except SafeExitRequested:
            print()
            print("입력이 중단되어 현재 데이터를 저장한 뒤 종료합니다.")
            self._save_state()

    def _print_title(self) -> None:
        print("=" * 40)
        print("        나만의 퀴즈 게임")
        print("=" * 40)

    def _print_menu(self) -> None:
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def _prompt_text(self, message: str) -> str:
        while True:
            raw_value = self._safe_input(message).strip()

            if raw_value:
                return raw_value

            print("입력이 비어 있습니다. 다시 입력해 주세요.")

    def _prompt_number(self, message: str, minimum: int, maximum: int) -> int:
        while True:
            raw_value = self._safe_input(message).strip()

            if not raw_value:
                print("입력이 비어 있습니다. 다시 입력해 주세요.")
                continue

            try:
                number = int(raw_value)
            except ValueError:
                print(
                    f"잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요."
                )
                continue

            if number < minimum or number > maximum:
                print(
                    f"허용 범위를 벗어났습니다. {minimum}-{maximum} 사이의 숫자를 입력하세요."
                )
                continue

            return number

    def _safe_input(self, message: str) -> str:
        try:
            return input(message)
        except (EOFError, KeyboardInterrupt) as error:
            raise SafeExitRequested from error

    def play_quiz(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없어 게임을 시작할 수 없습니다.")
            print()
            return

        selected_quizzes = random.sample(self.quizzes, k=len(self.quizzes))
        total_questions = len(selected_quizzes)
        correct_count = 0

        print(f"📝 퀴즈를 시작합니다! (총 {total_questions}문제, 랜덤 출제)")
        print()

        for index, quiz in enumerate(selected_quizzes, start=1):
            quiz.display(index)
            selected_answer = self._prompt_number("정답 입력 (1-4): ", 1, 4)

            if quiz.is_correct(selected_answer):
                correct_count += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

            print()

        points = int((correct_count / total_questions) * 100)
        result = {
            "points": points,
            "correct_count": correct_count,
            "total_questions": total_questions,
        }

        print("=" * 40)
        print(
            f"결과: {total_questions}문제 중 {correct_count}문제 정답! ({points}점)"
        )

        if self._is_new_best_score(result):
            self.best_score = result
            self._save_state()
            print("새로운 최고 점수입니다!")
        else:
            print("최고 점수는 유지되었습니다.")

        print("=" * 40)
        print()

    def add_quiz(self) -> None:
        print("새로운 퀴즈를 추가합니다.")
        question = self._prompt_text("문제를 입력하세요: ")
        choices = []

        for index in range(1, 5):
            choice = self._prompt_text(f"선택지 {index}: ")
            choices.append(choice)

        answer = self._prompt_number("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self._save_state()
        print("퀴즈가 추가되었습니다.")
        print()

    def show_quiz_list(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            print()
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("-" * 40)
        print()

    def show_best_score(self) -> None:
        if not self.best_score:
            print("아직 저장된 최고 점수가 없습니다. 먼저 퀴즈를 풀어 보세요.")
            print()
            return

        score_text = self._format_score(self.best_score)
        print(f"최고 점수: {score_text}")
        print()

    def _load_state(self) -> None:
        if not self.state_path.exists():
            self.quizzes = self._default_quizzes()
            self.best_score = None
            self.startup_message = (
                "state.json이 없어 기본 퀴즈 데이터로 새로 시작합니다."
            )
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
            self.startup_message = self._build_loaded_message()
        except (OSError, json.JSONDecodeError, ValueError, TypeError):
            self.quizzes = self._default_quizzes()
            self.best_score = None
            self.startup_message = (
                "state.json이 손상되었거나 읽을 수 없어 기본 데이터로 복구했습니다."
            )
            self._save_state()

    def _save_state(self) -> None:
        state = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

        try:
            with self.state_path.open("w", encoding="utf-8") as file:
                json.dump(state, file, ensure_ascii=False, indent=4)
        except OSError:
            print("파일 저장 중 문제가 발생했습니다. 권한과 경로를 확인해 주세요.")

    def _default_quizzes(self) -> list[Quiz]:
        return [Quiz.from_dict(quiz_data) for quiz_data in DEFAULT_QUIZ_DATA]

    def _load_quizzes(self, raw_quizzes: list[dict]) -> list[Quiz]:
        if not isinstance(raw_quizzes, list):
            raise ValueError("quizzes 데이터는 리스트여야 합니다.")

        quizzes = []
        for raw_quiz in raw_quizzes:
            quizzes.append(Quiz.from_dict(raw_quiz))

        return quizzes

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
            f"(퀴즈 {len(self.quizzes)}개, 최고 점수 {best_score_text})"
        )

    def _format_score(self, score: dict) -> str:
        if score["total_questions"] == 0:
            return f"{score['points']}점"

        return (
            f"{score['points']}점 "
            f"({score['total_questions']}문제 중 {score['correct_count']}문제 정답)"
        )
