class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self) -> None:
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, selected_answer: int) -> bool:
        return selected_answer == self.answer
