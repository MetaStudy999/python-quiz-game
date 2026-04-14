class Quiz:
    def __init__(
        self, question: str, choices: list[str], answer: int, hint: str = ""
    ) -> None:
        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer
        self.hint = hint.strip()
        self._validate()

    def _validate(self) -> None:
        if not self.question:
            raise ValueError("문제는 비어 있을 수 없습니다.")

        if len(self.choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")

        if any(not choice for choice in self.choices):
            raise ValueError("선택지는 비어 있을 수 없습니다.")

        if self.answer not in (1, 2, 3, 4):
            raise ValueError("정답 번호는 1부터 4 사이여야 합니다.")

    def display(self, number: int) -> None:
        print("-" * 40)
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, selected_answer: int) -> bool:
        return selected_answer == self.answer

    def has_hint(self) -> bool:
        return bool(self.hint)

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터 형식이 올바르지 않습니다.")

        raw_choices = data.get("choices", [])
        if not isinstance(raw_choices, list):
            raise ValueError("선택지 데이터는 리스트여야 합니다.")

        return cls(
            question=str(data.get("question", "")),
            choices=[str(choice) for choice in raw_choices],
            answer=int(data.get("answer", 0)),
            hint=str(data.get("hint", "")),
        )
