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
        while True:
            self.show_menu()
            selected_menu = self.prompt_number("선택: ", 1, 5)
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
                print("프로그램을 종료합니다.")
                break

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

    def prompt_number(self, message: str, minimum: int, maximum: int) -> int:
        while True:
            raw_value = input(message).strip()

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

    def play_quiz(self) -> None:
        print("퀴즈 풀기 기능을 준비 중입니다.")
        print()

    def add_quiz(self) -> None:
        print("퀴즈 추가 기능을 준비 중입니다.")
        print()

    def show_quiz_list(self) -> None:
        print(f"현재 등록된 퀴즈 수: {len(self.quizzes)}")
        print()

    def show_best_score(self) -> None:
        print(f"현재 최고 점수: {self.best_score}점")
        print()
