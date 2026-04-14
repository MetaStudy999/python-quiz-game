from quiz import Quiz


DEFAULT_QUIZ_DATA = [
    Quiz(
        "Python에서 문자열을 이어 붙일 때 사용하는 연산자는 무엇인가요?",
        ["+", "-", "*", "/"],
        1,
    ),
    Quiz(
        "다음 중 리스트를 나타내는 자료형 표기는 무엇인가요?",
        ["{}", "()", "[]", "<>"],
        3,
    ),
    Quiz(
        "조건이 참일 때만 코드를 실행하도록 만드는 문장은 무엇인가요?",
        ["for", "if", "while", "def"],
        2,
    ),
    Quiz(
        "Git에서 작업 내역을 저장하는 기록 단위를 무엇이라고 하나요?",
        ["clone", "branch", "commit", "pull"],
        3,
    ),
    Quiz(
        "원격 저장소의 변경 사항을 내 컴퓨터로 가져오는 Git 명령어는 무엇인가요?",
        ["push", "merge", "checkout", "pull"],
        4,
    ),
    Quiz(
        "함수를 정의할 때 사용하는 Python 키워드는 무엇인가요?",
        ["class", "return", "def", "import"],
        3,
    ),
]


class QuizGame:
    def __init__(self) -> None:
        self.quizzes = DEFAULT_QUIZ_DATA
        self.best_score = 0

    def run(self) -> None:
        self.show_title()
        self.show_menu()
        print("기능 구현을 준비 중입니다.")

    def show_title(self) -> None:
        print("=" * 40)
        print("        나만의 퀴즈 게임")
        print("=" * 40)

    def show_menu(self) -> None:
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)
