# Git과 함께하는 Python 첫 발자국

## 프로젝트 개요

이 프로젝트는 Python 기본 문법과 Git 기초를 함께 익히기 위한 콘솔 퀴즈 게임입니다.
사용자는 메뉴를 통해 퀴즈를 풀고, 새 퀴즈를 추가하고, 등록된 문제를 확인하고, 최고 점수를 관리할 수 있습니다.
데이터는 프로젝트 루트의 `state.json` 파일에 UTF-8 형식으로 저장되어 프로그램을 다시 실행해도 유지됩니다.
또한 콘솔 화면에서 상태에 맞는 이모티콘 아이콘과 컬러를 사용해 메뉴, 경고, 정답/오답, 힌트, 점수 메시지를 더 직관적으로 구분하도록 구성했습니다.

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
- 상태별 이모티콘 및 컬러 메시지 출력

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
- 정답, 오답, 경고, 저장 완료 같은 상태 메시지는 서로 다른 컬러로 구분되도록 구성했습니다.
- 터미널이 ANSI 컬러를 지원하지 않는 경우에는 일반 텍스트로 안전하게 표시됩니다.

## 제출용 프로젝트 설명

이 프로젝트는 Python과 Git 기초를 함께 연습하기 위해 만든 콘솔 퀴즈 게임입니다. `Quiz`와 `QuizGame` 클래스로 기능을 분리했고, `state.json`에 퀴즈 데이터, 최고 점수, 플레이 기록을 저장해 프로그램을 다시 실행해도 데이터가 유지되도록 구현했습니다. 기본 요구사항 외에도 랜덤 출제, 문제 수 선택, 힌트 기능, 퀴즈 삭제, 점수 히스토리 저장까지 보너스 과제를 반영했고, 콘솔 화면에는 상태에 맞는 이모티콘 아이콘과 컬러를 적용해 가독성을 높였습니다. 또한 기능 단위 커밋, 브랜치 생성 및 병합, `push`, `clone`, `pull`까지 직접 수행해 Git 워크플로우도 함께 연습했습니다.

## 스크린샷 설명 예시

- `env.png`: 개발 환경 설정 화면입니다. Python과 Git 버전, Git 사용자 설정이 정상적으로 적용된 것을 확인할 수 있습니다.

- `menu.png`: 프로그램 실행 후 메인 메뉴 화면입니다. 기능별 이모티콘 아이콘과 컬러가 적용되어 퀴즈 풀기, 추가, 목록, 점수 확인, 삭제, 종료 기능을 더 직관적으로 구분할 수 있습니다.

- `add_quiz.png`: 새로운 퀴즈를 직접 등록하는 화면입니다. 문제, 선택지 4개, 정답 번호를 입력하면 `state.json`에 저장됩니다.

- `list.png`: 현재 저장된 퀴즈 목록을 확인하는 화면입니다. 기본 퀴즈와 사용자가 추가한 퀴즈가 함께 표시됩니다.

- `play.png`: 퀴즈를 실제로 푸는 화면 또는 결과 화면입니다. 각 문제에 답을 입력하면 정답/오답/힌트 메시지가 아이콘과 컬러로 구분되어 표시되고, 마지막에는 총 정답 수와 점수가 출력됩니다.

- `score.png`: 최고 점수 확인 화면입니다. 점수와 최근 기록이 강조된 스타일로 표시되며, 이전 플레이 결과가 저장되어 프로그램을 다시 실행해도 최고 점수가 유지됩니다.

- `bonus.png`: 랜덤 출제, 문제 수 선택, 힌트 사용, 퀴즈 삭제, 점수 기록 히스토리와 함께 상태별 아이콘 및 컬러 메시지가 보이는 화면입니다.

- `git-log.png`: `git log --oneline --graph --decorate --all` 실행 결과입니다. 기능 단위 커밋과 브랜치 생성 및 병합 기록을 확인할 수 있습니다.

- `github-repo.png`: GitHub 원격 저장소 화면입니다. 프로젝트 코드와 README가 업로드된 상태를 확인할 수 있습니다.

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
