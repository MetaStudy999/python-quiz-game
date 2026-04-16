from quiz_game import QuizGame


def main() -> None:
    # QuizGame 인스턴스가 메뉴 출력부터 저장까지 전체 흐름을 관리합니다.
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()
