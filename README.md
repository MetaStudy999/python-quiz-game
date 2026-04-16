# Git과 함께하는 Python 첫 발자국

## 프로젝트 개요

이 프로젝트는 Python 기본 문법과 Git 기초를 함께 익히기 위한 콘솔 퀴즈 게임입니다.
사용자는 메뉴를 통해 퀴즈를 풀고, 새 퀴즈를 추가하고, 등록된 문제를 확인하고, 최고 점수를 관리할 수 있습니다.
데이터는 프로젝트 루트의 `state.json` 파일에 UTF-8 형식으로 저장되어 프로그램을 다시 실행해도 유지됩니다.
또한 콘솔 화면에서 상태에 맞는 이모티콘 아이콘을 사용해 메뉴, 경고, 정답/오답, 힌트, 점수 메시지를 더 직관적으로 구분하도록 구성했습니다.

## 퀴즈 주제와 선정 이유

퀴즈 주제는 **Python과 Git 입문**입니다.
이번 미션의 핵심 학습 주제와 직접 연결되어 있어, 프로그램을 만들면서 동시에 관련 개념도 함께 복습할 수 있도록 구성했습니다.

## 과제 목표

### Python 기초

- 변수: 값을 저장해 두는 이름표입니다. 같은 값을 여러 번 쓰거나, 나중에 값을 바꿔 다시 사용할 때 편합니다.
- `int`: 정수를 저장하는 자료형입니다. 예: `1`, `10`, `100`
- `str`: 글자나 문장을 저장하는 자료형입니다. 예: `"Python"`, `"정답입니다"`
- `bool`: 참과 거짓을 나타내는 자료형입니다. 예: `True`, `False`
- `list`: 여러 값을 순서대로 묶어 저장하는 자료형입니다. 예: 선택지 목록, 퀴즈 목록
- `dict`: 이름표(키)와 값(value)을 짝으로 저장하는 자료형입니다. 예: `state.json`의 퀴즈 데이터
- `if/elif/else`: 조건에 따라 다른 코드를 실행하는 문장입니다. 예를 들어 정답이면 정답 메시지를, 아니면 오답 메시지를 보여 줄 수 있습니다.
- `for`: 정해진 묶음을 처음부터 끝까지 하나씩 꺼내며 반복할 때 사용합니다. 예: 퀴즈 목록 출력
- `while`: 조건이 참인 동안 계속 반복할 때 사용합니다. 예: 올바른 입력이 들어올 때까지 다시 묻기
- 함수: 자주 쓰는 동작을 이름 붙여 묶어 둔 기능입니다. 코드를 짧고 읽기 쉽게 만들 수 있습니다.
- 매개변수: 함수를 실행할 때 함수 안으로 전달하는 값입니다. 예: 문제 번호, 안내 문구
- 반환값: 함수가 실행을 마친 뒤 바깥으로 돌려주는 결과값입니다. 예: 사용자가 입력한 숫자

현재 코드 예시:

```python
question_count = self._select_question_count()
selected_quizzes = random.sample(self.quizzes, k=question_count)

for index, quiz in enumerate(selected_quizzes, start=1):
    selected_answer, used_hint = self._prompt_answer_with_hint(quiz)
    if quiz.is_correct(selected_answer):
        correct_count += 1
```

위 코드는 변수(`question_count`), 정수(`correct_count`), 리스트(`selected_quizzes`), 조건문(`if`), 반복문(`for`), 함수 호출(`self._select_question_count()`)이 실제로 어떻게 함께 쓰이는지 보여 줍니다.

### 클래스와 객체

- 클래스: 비슷한 데이터와 기능을 한 틀로 묶어 두는 설계도입니다. 예: `Quiz`, `QuizGame`
- 객체: 클래스를 바탕으로 실제로 만들어진 결과물입니다. 예: 하나의 퀴즈 문제
- `__init__`: 객체가 처음 만들어질 때 필요한 값을 넣어 주는 특별한 메서드입니다.
- `self`: 지금 사용 중인 객체 자기 자신을 가리킵니다. 객체 안의 속성과 메서드에 접근할 때 사용합니다.
- 속성(attribute): 객체가 가지고 있는 데이터입니다. 예: 문제, 선택지, 정답, 힌트
- 메서드(method): 객체가 할 수 있는 동작입니다. 예: 퀴즈 출력, 정답 확인, 게임 시작

현재 코드 예시:

```python
class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int, hint: str = "") -> None:
        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer
        self.hint = hint.strip()

game = QuizGame()
game.run()
```

위 코드는 `Quiz`와 `QuizGame`이 클래스이고, `game = QuizGame()`처럼 실제로 만든 값이 객체라는 점을 보여 줍니다. `self.question`, `self.answer`는 속성이고, `run()`은 메서드입니다.

### 파일 입출력

- 파일 열기: 저장된 내용을 읽거나 새 내용을 쓰기 위해 파일을 사용하는 첫 단계입니다.
- 파일 읽기: 파일 안의 데이터를 프로그램으로 가져오는 과정입니다. 예: `state.json` 불러오기
- 파일 쓰기: 프로그램에서 만든 데이터를 파일에 저장하는 과정입니다. 예: 퀴즈 추가 후 저장
- JSON: 리스트와 딕셔너리처럼 구조화된 데이터를 저장하기 좋은 형식입니다. 사람이 읽기 쉽고 프로그램도 다루기 쉽습니다.
- `state.json`: 퀴즈 목록, 최고 점수, 점수 기록을 저장하는 프로젝트의 데이터 파일입니다.
- `try/except`: 오류가 나더라도 프로그램이 갑자기 종료되지 않도록 대비하는 문법입니다. 예: 파일이 없거나 JSON이 손상된 경우 처리

간단한 문법 예시:

파일 열기:

```python
with open("state.json", "r", encoding="utf-8") as file:
    print("파일을 열었습니다.")
```

파일 읽기:

```python
with open("state.json", "r", encoding="utf-8") as file:
    text = file.read()
```

파일 쓰기:

```python
with open("memo.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요")
```

JSON 읽기/쓰기:

```python
import json

with open("state.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open("state.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
```

`try/except` 예시:

```python
try:
    with open("state.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"quizzes": [], "best_score": None, "score_history": []}
except json.JSONDecodeError:
    data = {"quizzes": [], "best_score": None, "score_history": []}
```

현재 프로젝트 코드 예시:

```python
try:
    with self.state_path.open("w", encoding="utf-8") as file:
        json.dump(state, file, ensure_ascii=False, indent=4)
except OSError:
    print(self._error_text("파일 저장 중 문제가 발생했습니다. 권한과 경로를 확인해 주세요."))
```

위 코드는 이 프로젝트에서 `state.json` 파일을 UTF-8로 저장하는 실제 부분입니다. 기본 `open()` 대신 `Path.open()`을 사용했고, `json.dump()`로 딕셔너리 데이터를 JSON으로 저장하며, `try/except`로 저장 오류까지 처리합니다.

### Git 기초

- Git: 파일 변경 이력을 기록하는 도구입니다. 무엇을 언제 바꿨는지 남기고 되돌아보기에 좋습니다.
- `init`: 현재 폴더를 Git 저장소로 시작하는 명령어입니다. 예: `git init`
- `add`: 다음 커밋에 포함할 파일을 선택하는 명령어입니다. 예: `git add README.md`, `git add .`
- `commit`: 선택한 변경 내용을 하나의 기록으로 저장하는 명령어입니다. 예: `git commit -m "Feat: 퀴즈 출제 기능 구현"`
- `push`: 내 컴퓨터의 커밋을 GitHub 같은 원격 저장소로 올리는 명령어입니다. 예: `git push origin main`
- `pull`: 원격 저장소의 최신 변경 내용을 내 컴퓨터로 가져오는 명령어입니다. 예: `git pull origin main`
- `checkout`: 다른 브랜치로 이동하거나 새 브랜치를 만들어 전환할 때 사용하는 명령어입니다. 예: `git checkout -b feature/play-quiz`, `git checkout main`
- `clone`: 원격 저장소를 내 컴퓨터로 그대로 복제하는 명령어입니다. 예: `git clone https://github.com/MetaStudy999/python-quiz-game.git`
- 브랜치(branch): 메인 작업과 분리해서 새 기능을 안전하게 개발하는 작업 공간입니다. 예: `feature/play-quiz`
- `merge`: 브랜치에서 작업한 내용을 다시 `main` 브랜치에 합치는 과정입니다. 예: `git merge feature/play-quiz`

이 프로젝트에서 실제 사용한 예시:

```bash
git checkout -b feature/play-quiz
git commit -m "Feat: 퀴즈 출제 기능 구현"
git checkout main
git merge feature/play-quiz
git push origin main
git clone https://github.com/MetaStudy999/python-quiz-game.git
git pull origin main
```

위 명령들은 이 프로젝트를 개발하면서 실제로 사용한 흐름입니다. 브랜치를 나눠 기능을 만들고, `merge`로 합친 뒤, GitHub에 `push`하고 다시 `clone`과 `pull`까지 수행했습니다.

## 실행 방법

1. Python 3.10 이상이 설치되어 있는지 확인합니다.
2. 프로젝트 루트에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 삭제
- 퀴즈 목록 확인
- 최고 점수 확인
- 최근 점수 기록 확인
- `state.json` 저장 및 불러오기
- 잘못된 입력 재처리
- `Ctrl+C`, `EOF` 발생 시 안전 종료
- 데이터 파일 손상 시 기본 데이터 복구
- 랜덤 출제
- 문제 수 선택
- 힌트 사용 및 점수 차감
- 상태별 이모티콘 메시지 출력

## 기능 요구 사항 체크리스트

1. Git 저장소 설정: 완료. `.gitignore`, `README.md`, 초기 커밋, GitHub `push`까지 반영했습니다.
2. 메뉴 기능: 완료. 프로그램 시작 시 메뉴를 출력하고, 번호 선택과 종료 기능을 제공합니다.
3. 공통 입력/예외 처리: 완료. 공백 제거, 숫자 변환 실패, 범위 밖 입력, 빈 입력, `Ctrl+C`, `EOFError`, 손상된 데이터 파일 복구를 처리합니다.
4. `Quiz` 클래스: 완료. 문제, 선택지, 정답, 힌트 속성과 출력 및 정답 확인 메서드를 구현했습니다.
5. 기본 퀴즈 데이터: 완료. Python과 Git 입문 주제의 기본 퀴즈 6개를 포함했습니다.
6. 퀴즈 풀기: 완료. 별도 브랜치 작업 기록이 있고, 퀴즈 출제, 정답 입력, 결과 표시가 동작합니다.
7. 퀴즈 추가: 완료. 문제, 선택지 4개, 힌트, 정답 번호를 입력받아 저장합니다.
8. 퀴즈 목록: 완료. 현재 저장된 퀴즈 목록을 확인할 수 있고, 비어 있는 경우도 처리합니다.
9. 점수 확인: 완료. 최고 점수와 최근 기록을 확인할 수 있고, 플레이 후 자동 갱신됩니다.
10. `QuizGame` 클래스: 완료. 메뉴 표시, 게임 진행, 추가, 목록, 점수, 삭제, 저장/불러오기를 통합 관리합니다.
11. 파일 저장/불러오기: 완료. 프로젝트 루트 `state.json`에 UTF-8로 저장하며, 파일이 없거나 손상된 경우 기본 데이터로 복구합니다.
12. `README.md` 작성: 완료. 프로젝트 개요, 주제 이유, 실행 방법, 기능 목록, 파일 구조, 데이터 파일 설명, 과제 목표를 포함했습니다.
13. Git 저장소 복제 실습: 완료. 실제로 `clone`, 복제본 수정 후 `push`, 원래 저장소에서 `pull`까지 수행했습니다.

## 파일 구조

```text
python-quiz-game/
├── .gitignore
├── README.md
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
└── docs/
    └── screenshots/
```

## 데이터 파일 설명

- 경로: 프로젝트 루트의 `state.json`
- 역할: 퀴즈 목록과 최고 점수를 저장합니다.
- 인코딩: UTF-8

예시 스키마:

```json
{
    "quizzes": [
        {
            "question": "Python의 창시자는 누구인가요?",
            "choices": ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],
            "answer": 1,
            "hint": "Python을 만든 사람의 이름입니다."
        }
    ],
    "best_score": {
        "points": 80,
        "correct_count": 4,
        "total_questions": 5,
        "hints_used": 1
    },
    "score_history": [
        {
            "played_at": "2026-04-14 20:10:00",
            "total_questions": 5,
            "correct_count": 4,
            "points": 80,
            "hints_used": 1
        }
    ]
}
```

## 보너스 기능 반영 내용

- 랜덤 출제: 퀴즈를 시작할 때마다 문제 순서를 섞어서 출제합니다.
- 문제 수 선택: 플레이 시작 전에 이번에 풀 문제 수를 직접 선택할 수 있습니다.
- 힌트 기능: 문제마다 힌트를 볼 수 있고, 힌트를 사용하면 점수에서 차감됩니다.
- 퀴즈 삭제 기능: 등록된 퀴즈를 번호로 선택해 삭제할 수 있습니다.
- 점수 기록 히스토리: 플레이 날짜, 문제 수, 정답 수, 점수를 `state.json`에 누적 저장합니다.

## 콘솔 UI 표현

- 메뉴, 점수, 힌트, 삭제, 종료 등 기능 성격에 맞는 이모티콘 아이콘을 적용했습니다.
- 정답, 오답, 경고, 저장 완료 같은 상태 메시지는 아이콘과 문구 차이로 쉽게 구분되도록 구성했습니다.

## 제출용 프로젝트 설명

이 프로젝트는 Python과 Git 기초를 함께 연습하기 위해 만든 콘솔 퀴즈 게임입니다. `Quiz`와 `QuizGame` 클래스로 기능을 분리했고, `state.json`에 퀴즈 데이터, 최고 점수, 플레이 기록을 저장해 프로그램을 다시 실행해도 데이터가 유지되도록 구현했습니다. 기본 요구사항 외에도 랜덤 출제, 문제 수 선택, 힌트 기능, 퀴즈 삭제, 점수 히스토리 저장까지 보너스 과제를 반영했고, 콘솔 화면에는 상태에 맞는 이모티콘 아이콘을 적용해 가독성을 높였습니다. 또한 기능 단위 커밋, 브랜치 생성 및 병합, `push`, `clone`, `pull`까지 직접 수행해 Git 워크플로우도 함께 연습했습니다.

## 코드 구조 및 설계 설명

### `Quiz`와 `QuizGame`의 책임 분리

| 클래스 | 맡은 역할 | 이유 |
| --- | --- | --- |
| `Quiz` | 문제 1개의 데이터 보관, 데이터 검증, 문제 출력, 정답 확인, JSON 변환 | 퀴즈 1개 자체의 규칙을 한곳에 모으면 재사용과 검증이 쉬워집니다. |
| `QuizGame` | 메뉴 출력, 사용자 입력, 게임 진행, 점수 계산, 저장/불러오기, 종료 처리 | 여러 퀴즈를 모아 실제 게임으로 운영하는 흐름을 한곳에서 관리할 수 있습니다. |

쉽게 말해 `Quiz`는 "문제 한 개"를 책임지고, `QuizGame`은 "프로그램 전체 진행"을 책임집니다.  
이렇게 나누면 문제 데이터 형식이 바뀌어도 `Quiz`를 먼저 보면 되고, 메뉴나 저장 방식이 바뀌면 `QuizGame`을 먼저 보면 되어 수정 범위가 더 분명해집니다.

### 입력 처리, 게임 진행, 저장/불러오기 로직을 나눈 기준

- 입력 처리(검증)는 "`사용자가 무엇을 입력하든 프로그램이 안전하게 받아들이게 하는 일`"로 보고 `QuizGame._prompt_text()`, `QuizGame._prompt_number()`, `QuizGame._safe_input()`에 모았습니다.
- 게임 진행은 "`입력이 이미 정상이라는 가정 아래 실제 기능을 수행하는 일`"로 보고 `play_quiz()`, `add_quiz()`, `delete_quiz()`, `show_quiz_list()`, `show_best_score()`에 나눴습니다.
- 데이터 저장/불러오기는 "`프로그램 바깥 파일과 통신하는 일`"로 보고 `_load_state()`, `_save_state()`, `_load_quizzes()`, `_load_best_score()`, `_load_score_history()`에 모았습니다.
- 퀴즈 데이터 자체의 형식 검사는 `Quiz._validate()`와 `Quiz.from_dict()`가 맡습니다. 즉, 사용자 입력 검증과 파일 데이터 검증도 성격이 달라 따로 분리했습니다.

이 기준의 핵심은 "무엇이 바뀔 때 어떤 코드를 먼저 봐야 하는가"입니다.  
입력 규칙이 바뀌면 입력 메서드, 게임 규칙이 바뀌면 진행 메서드, 파일 형식이 바뀌면 저장 메서드를 먼저 수정하면 됩니다.

### `state.json` 읽기/쓰기 흐름

프로그램 안에서 `state.json`은 아래 순서로 사용됩니다.

1. `main.py`에서 `QuizGame()` 객체를 만듭니다.
2. `QuizGame.__init__()`가 실행되면서 바로 `_load_state()`를 호출합니다.
3. `state.json`이 있으면 JSON을 읽고, `quizzes`, `best_score`, `score_history`를 각각 메서드로 검증하며 메모리로 올립니다.
4. `state.json`이 없으면 기본 퀴즈를 만든 뒤 `_save_state()`를 호출해 새 파일을 바로 생성합니다.
5. 파일이 손상되었거나 구조가 잘못되었으면 기본 데이터로 복구한 뒤 `_save_state()`로 다시 저장합니다.
6. 사용자가 퀴즈를 풀면 `play_quiz()`가 점수와 기록을 갱신하고 `_save_state()`를 호출합니다.
7. 사용자가 퀴즈를 추가하면 `add_quiz()`가 목록에 넣고 `_save_state()`를 호출합니다.
8. 사용자가 퀴즈를 삭제하면 `delete_quiz()`가 목록에서 제거하고 `_save_state()`를 호출합니다.
9. 사용자가 종료 메뉴를 고르면 `run()`이 `_save_state()`를 한 번 더 호출한 뒤 종료합니다.
10. 입력 중 `Ctrl+C` 또는 `EOF`가 발생해도 `run()`의 예외 처리에서 `_save_state()`를 호출하고 종료합니다.

즉, 이 프로그램은 "시작할 때 읽고, 데이터가 바뀔 때마다 저장하고, 종료할 때 한 번 더 저장하는 방식"으로 동작합니다.

### `Ctrl+C` / `EOF` 안전 종료 처리

현재 구현에서는 `input()`을 직접 곳곳에서 호출하지 않고 `QuizGame._safe_input()`으로 감쌌습니다.

- 사용자가 `Ctrl+C`를 누르면 `KeyboardInterrupt`가 발생합니다.
- 입력 스트림이 끝나면 `EOFError`가 발생합니다.
- `_safe_input()`은 이 두 예외를 직접 종료로 처리하지 않고 `SafeExitRequested`라는 커스텀 예외로 바꿔 `run()`까지 전달합니다.
- `run()`은 이 예외를 잡아 경고 메시지를 보여 주고 `_save_state()`를 호출한 뒤 종료합니다.

이 방식의 장점은 종료 규칙이 한곳에 모인다는 점입니다.  
입력 함수마다 따로 종료 코드를 쓰지 않아도 되고, "중단되면 저장 후 종료"라는 정책을 일관되게 적용할 수 있습니다.

더 안전하게 만들고 싶다면 아래 보완도 가능합니다.

- 저장할 때 임시 파일에 먼저 쓴 뒤 마지막에 파일 이름을 바꾸는 방식(원자적 저장)을 사용합니다.
- 저장 직전 기존 `state.json`을 백업 파일로 복사해 둡니다.
- 프로그램 강제 종료가 저장 도중 발생해도 마지막 정상 파일을 복구할 수 있게 합니다.

### 커밋 단위와 커밋 메시지 규칙

현재 Git 로그를 보면 커밋을 "기능 하나", "문서 작업 하나", "리팩터링 하나"처럼 작은 의미 단위로 나눴습니다.

- `Init: 프로젝트 기본 파일 생성`
- `Feat: Quiz 클래스 구현`
- `Feat: 퀴즈 출제 기능 구현`
- `Feat: state.json 저장 기능 추가`
- `Refactor: 예외 처리와 데이터 복구 로직 강화`
- `Docs: README에 현재 코드 예시 추가`

이 프로젝트의 메시지 규칙은 `타입: 짧은 설명` 형식입니다.

- `Init`: 프로젝트 시작
- `Feat`: 사용자 입장에서 보이는 기능 추가
- `Refactor`: 기능은 같지만 구조 개선
- `Docs`: README나 문서 수정
- `Style`: 출력 모양이나 표현 정리
- `Merge`: 브랜치 병합 기록
- `Delete`: 불필요한 파일 제거

이 규칙을 쓰면 `git log --oneline`만 봐도 "무슨 종류의 변경인지"를 빠르게 파악할 수 있습니다.

## 핵심 기술 원리 적용

### 클래스를 사용한 이유와 함수만으로 구현할 때의 차이

이 프로젝트는 퀴즈 데이터와 게임 상태가 계속 함께 움직이기 때문에 클래스를 사용했습니다.

- `Quiz` 객체는 문제, 선택지, 정답, 힌트라는 데이터를 한 묶음으로 보관합니다.
- `QuizGame` 객체는 퀴즈 목록, 최고 점수, 기록, 저장 경로를 한곳에 보관합니다.
- 같은 데이터에 항상 함께 쓰이는 기능도 메서드로 가까이 둡니다. 예를 들어 `Quiz.is_correct()`는 정답 데이터와 바로 연결됩니다.

함수만으로도 만들 수는 있지만 차이가 있습니다.

- 함수만 사용하면 `quizzes`, `best_score`, `score_history`, `state_path`를 매번 인자로 넘기거나 전역 변수로 관리해야 할 가능성이 큽니다.
- 데이터와 기능이 여러 파일에 흩어지기 쉬워져서 "이 값은 누가 책임지는가"가 흐려질 수 있습니다.
- 클래스는 관련 데이터와 기능을 함께 묶어 실수 가능성을 줄이고, 코드를 읽을 때도 구조가 더 잘 보입니다.

즉, 작은 프로젝트라도 "상태가 있는 프로그램"은 클래스로 묶으면 관리가 더 쉬워집니다.

### JSON 파일로 저장한 이유와 JSON 형식의 특징

이 프로젝트에서 JSON을 선택한 이유는 학습용 프로젝트에 가장 단순하고 이해하기 쉬운 저장 방식이기 때문입니다.

- Python 기본 `json` 모듈로 바로 읽고 쓸 수 있습니다.
- 사람이 열어 봐도 구조를 이해하기 쉽습니다.
- 딕셔너리와 리스트를 그대로 옮기기 좋아 퀴즈 목록, 최고 점수, 기록 저장에 잘 맞습니다.
- 언어에 크게 종속되지 않아 나중에 다른 프로그램으로도 읽기 쉽습니다.

JSON 형식의 특징도 함께 이해하면 좋습니다.

- 텍스트 기반이라 수정과 확인이 쉽습니다.
- 객체와 배열의 중첩 구조를 표현할 수 있습니다.
- 숫자, 문자열, 참/거짓, 리스트, 객체처럼 기본 자료형 저장에 적합합니다.
- 반면 주석이 없고, 아주 큰 데이터나 동시 접근이 많은 상황에는 데이터베이스보다 불리합니다.

### 파일 입출력에서 `try/except`가 필요한 이유

파일은 프로그램 바깥 세상과 연결되어 있기 때문에, 내 코드가 맞아도 실패할 수 있습니다.  
그래서 파일 입출력에는 `try/except`가 중요합니다.

이 프로젝트에서 실제로 대비하는 실패 케이스는 아래와 같습니다.

- `FileNotFoundError`에 해당하는 상황: 첫 실행이라 `state.json`이 아직 없을 수 있습니다.
- `json.JSONDecodeError`: 파일은 있지만 JSON 문법이 깨져 있을 수 있습니다.
- `OSError`: 읽기/쓰기 권한이 없거나, 경로가 잘못되었거나, 디스크 문제로 저장이 실패할 수 있습니다.
- `ValueError`, `TypeError`: JSON 문법은 맞아도 내부 값이 기대한 형식이 아닐 수 있습니다. 예를 들어 `choices`가 리스트가 아니라 문자열일 수 있습니다.

즉, `try/except`는 "오류를 숨기기 위한 장치"가 아니라 "문제가 생겨도 프로그램이 예측 가능한 방식으로 복구되게 하는 장치"입니다.

### 브랜치를 분리해 작업한 이유와 병합(merge)의 의미

이 프로젝트에서는 실제로 `feature/play-quiz`, `feature/persistence` 브랜치를 만들고, 이후 `main`으로 합쳤습니다.

- 브랜치를 나누면 아직 완성되지 않은 작업이 `main`을 망가뜨리지 않습니다.
- 기능별 작업 내역이 분리되어 어떤 변경이 어디서 일어났는지 추적하기 쉽습니다.
- 실험이나 수정이 실패해도 메인 흐름에 바로 영향을 주지 않습니다.

`merge`는 따로 작업하던 브랜치의 변경 내용을 기준 브랜치에 합치는 과정입니다.  
예를 들어 `feature/persistence`에서 `state.json` 저장 기능을 만든 뒤 `main`에 병합하면, 이제 메인 코드도 그 기능을 갖게 됩니다.

쉽게 말해 브랜치는 "분리된 작업 공간"이고, 병합은 "검토가 끝난 작업을 메인 흐름에 반영하는 일"입니다.

### `state.json` 데이터 구조를 현재 형태로 설계한 이유

현재 `state.json`의 최상위 구조는 객체 하나이고, 그 안에 세 가지 큰 정보를 넣었습니다.

| 필드 | 형태 | 이유 |
| --- | --- | --- |
| `quizzes` | 퀴즈 객체의 리스트 | 문제는 여러 개이므로 순서 있는 목록으로 관리하는 것이 자연스럽습니다. |
| `best_score` | 점수 요약 객체 또는 `null` | 최고 점수는 한 개만 빠르게 꺼내 쓰면 되므로 별도 필드로 두었습니다. |
| `score_history` | 기록 객체의 리스트 | 플레이할 때마다 한 줄씩 누적되는 데이터이므로 리스트가 잘 맞습니다. |

퀴즈 하나를 다시 객체로 중첩한 이유도 있습니다.

- `question`, `choices`, `answer`, `hint`는 서로 떨어질 수 없는 한 문제의 구성 요소입니다.
- `choices`를 리스트로 두면 같은 문제 안에서 보기 순서를 유지할 수 있습니다.
- `answer`를 번호로 저장하면 정답 비교가 단순해집니다.
- `hint`를 같은 객체 안에 두면 문제별 추가 정보를 쉽게 확장할 수 있습니다.

즉, 현재 구조는 "사람이 읽기 쉽고, Python 딕셔너리/리스트로 바로 옮기기 쉽고, 작은 프로젝트에 충분히 단순한 구조"를 목표로 설계한 것입니다.

## 심층 인터뷰 대비 설명

### 퀴즈 데이터가 1000개 이상으로 늘어날 때 JSON 저장 방식의 한계

현재 방식은 작은 프로젝트에는 충분하지만, 데이터가 크게 늘어나면 한계가 보이기 시작합니다.

- 시작할 때 파일 전체를 한 번에 읽어야 하므로 로딩 시간이 길어질 수 있습니다.
- 퀴즈 하나만 추가하거나 삭제해도 파일 전체를 다시 써야 하므로 저장 비용이 커집니다.
- `score_history`까지 계속 커지면 파일 크기가 빠르게 늘어납니다.
- 두 프로그램이 동시에 같은 파일을 수정하면 마지막에 저장한 쪽이 이전 내용을 덮어쓸 위험이 있습니다.
- 검색, 필터링, 통계 집계가 많아지면 리스트 전체를 매번 순회해야 해 비효율적입니다.
- 파일이 한 번 손상되면 영향 범위가 전체 데이터로 번집니다.

데이터가 많아진다면 다음 단계로는 SQLite 같은 데이터베이스를 고려할 수 있습니다.  
그러면 필요한 데이터만 읽고 쓰기 쉬워지고, 검색과 정렬도 더 효율적으로 처리할 수 있습니다.

### `state.json`이 손상되었을 때 데이터 손실을 줄이는 대응 방법

현재 코드의 대응은 "프로그램이 죽지 않게 기본 데이터로 복구해서 다시 시작"하는 방식입니다.  
장점은 실행이 막히지 않는다는 점이지만, 단점은 손상 전 사용자 데이터가 사라질 수 있다는 점입니다.

데이터 손실을 더 줄이려면 아래 방법을 적용할 수 있습니다.

- 저장 직전에 기존 파일을 `state.json.bak`처럼 백업해 둡니다.
- 저장은 임시 파일에 먼저 쓴 뒤 성공하면 원본과 교체합니다.
- 파싱 실패 시 손상 파일을 바로 덮어쓰지 말고 `state-corrupted-날짜.json`처럼 이름을 바꿔 보관합니다.
- 백업 파일이 있으면 최근 정상 백업을 자동으로 복구합니다.
- 복구에 실패하면 기본 데이터로 초기화하되, 사용자에게 백업 위치와 초기화 사실을 알려 줍니다.

실무에서는 "파일이 깨져도 최소한 마지막 정상본은 남긴다"가 매우 중요합니다.

### 요구사항이 바뀔 때 먼저 수정할 파일과 메서드

요구사항이 바뀌면 모든 파일을 한 번에 보는 것보다, 규칙이 모여 있는 시작점을 먼저 찾는 것이 중요합니다.

| 변경 요구사항 | 먼저 볼 곳 | 이유 |
| --- | --- | --- |
| 점수 계산 방식 변경 | `quiz_game.py`의 `QuizGame.play_quiz()` | 현재 점수 계산과 힌트 감점이 이 메서드에 모여 있습니다. |
| 최고 점수 비교 기준 변경 | `quiz_game.py`의 `_is_new_best_score()` | 최고 점수 판정 규칙이 여기 있습니다. |
| 점수 저장 형식 변경 | `quiz_game.py`의 `_append_score_history()`, `_load_best_score()`, `_load_score_history()` | 저장 구조와 복원 구조를 함께 맞춰야 합니다. |
| 선택지 개수 변경 | `quiz.py`의 `Quiz._validate()`, `Quiz.from_dict()` | 현재는 "선택지 4개, 정답 1~4" 규칙이 고정되어 있습니다. |
| 선택지 입력 방식 변경 | `quiz_game.py`의 `add_quiz()`, `_prompt_answer_with_hint()` | 사용자 입력 개수와 허용 범위 안내 문구가 여기 들어 있습니다. |
| 문서와 예시 구조 변경 | `README.md`, `state.json` 예시 | 실제 코드와 문서 설명을 함께 맞춰야 혼란이 없습니다. |

예를 들어 선택지가 4개에서 5개로 늘어나면 `Quiz.display()`는 이미 리스트를 순회하므로 거의 그대로 사용할 수 있습니다.  
반대로 입력 검증과 정답 범위는 아직 `1-4`로 고정되어 있어 그 부분을 먼저 수정해야 합니다.

## 스크린샷 설명 예시

- [`env.png`](docs/screenshots/env.png): 개발 환경 설정 화면입니다. Python과 Git 버전, Git 사용자 설정이 정상적으로 적용된 것을 확인할 수 있습니다.

- [`menu.png`](docs/screenshots/menu.png): 프로그램 실행 후 메인 메뉴 화면입니다. 기능별 이모티콘 아이콘이 적용되어 퀴즈 풀기, 추가, 목록, 점수 확인, 삭제, 종료 기능을 더 직관적으로 구분할 수 있습니다.

- [`add_quiz.png`](docs/screenshots/add_quiz.png): 새로운 퀴즈를 직접 등록하는 화면입니다. 문제, 선택지 4개, 정답 번호를 입력하면 `state.json`에 저장됩니다.

- [`list.png`](docs/screenshots/list.png): 현재 저장된 퀴즈 목록을 확인하는 화면입니다. 기본 퀴즈와 사용자가 추가한 퀴즈가 함께 표시됩니다.

- [`play.png`](docs/screenshots/play.png): 퀴즈를 실제로 푸는 화면 또는 결과 화면입니다. 각 문제에 답을 입력하면 정답/오답/힌트 메시지가 아이콘으로 구분되어 표시되고, 마지막에는 총 정답 수와 점수가 출력됩니다.

- [`score.png`](docs/screenshots/score.png): 최고 점수 확인 화면입니다. 점수와 최근 기록이 강조된 스타일로 표시되며, 이전 플레이 결과가 저장되어 프로그램을 다시 실행해도 최고 점수가 유지됩니다.

- [`bonus.png`](docs/screenshots/bonus.png): 랜덤 출제, 문제 수 선택, 힌트 사용, 퀴즈 삭제, 점수 기록 히스토리와 함께 상태별 아이콘 메시지가 보이는 화면입니다.

- [`git-log.png`](docs/screenshots/git-log.png): `git log --oneline --graph --decorate --all` 실행 결과입니다. 기능 단위 커밋과 브랜치 생성 및 병합 기록을 확인할 수 있습니다.

- [`github-repo.png`](docs/screenshots/github-repo.png): GitHub 원격 저장소 화면입니다. 프로젝트 코드와 README가 업로드된 상태를 확인할 수 있습니다.

## 추천 Git 작업 순서

아래 순서대로 진행하면 미션 요구사항의 커밋 흐름을 자연스럽게 만들 수 있습니다.

1. `git add .`
2. `git commit -m "Init: 프로젝트 기본 파일 생성"`
3. `git commit -m "Feat: Quiz 클래스 구현"`
4. `git commit -m "Feat: 기본 퀴즈 데이터 추가"`
5. `git checkout -b feature/play-quiz`
6. `git commit -m "Feat: 퀴즈 출제 기능 구현"`
7. `git checkout main`
8. `git merge feature/play-quiz`
9. `git commit -m "Feat: 퀴즈 추가 기능 구현"`
10. `git commit -m "Feat: 퀴즈 목록 기능 구현"`
11. `git commit -m "Feat: 최고 점수 기능 구현"`
12. `git commit -m "Feat: state.json 저장 및 복구 로직 구현"`
13. `git commit -m "Docs: README 문서화"`

## clone / pull 실습 예시

1. GitHub에 저장소를 `push`합니다.
2. 다른 디렉터리에서 저장소를 복제합니다.

```bash
git clone <GitHub 저장소 URL>
```

3. 복제한 디렉터리에서 README에 한 줄을 추가한 뒤 커밋하고 `push`합니다.
4. 원래 작업 디렉터리로 돌아와 아래 명령어로 변경 사항을 가져옵니다.

```bash
git pull
```

실습 메모: GitHub에서 `clone`한 복제본으로 README를 수정한 뒤 `push`했고, 원래 작업 디렉터리에서 `pull`로 반영을 확인했습니다.
