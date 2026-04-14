# Git과 함께하는 Python 첫 발자국

## 프로젝트 개요

이 프로젝트는 Python 기본 문법과 Git 기초를 함께 익히기 위한 콘솔 퀴즈 게임입니다.
사용자는 메뉴를 통해 퀴즈를 풀고, 새 퀴즈를 추가하고, 등록된 문제를 확인하고, 최고 점수를 관리할 수 있습니다.
데이터는 프로젝트 루트의 `state.json` 파일에 UTF-8 형식으로 저장되어 프로그램을 다시 실행해도 유지됩니다.

## 퀴즈 주제와 선정 이유

퀴즈 주제는 **Python과 Git 입문**입니다.
이번 미션의 핵심 학습 주제와 직접 연결되어 있어, 프로그램을 만들면서 동시에 관련 개념도 함께 복습할 수 있도록 구성했습니다.

## 실행 방법

1. Python 3.10 이상이 설치되어 있는지 확인합니다.
2. 프로젝트 루트에서 아래 명령어를 실행합니다.

```bash
python3 main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- `state.json` 저장 및 불러오기
- 잘못된 입력 재처리
- `Ctrl+C`, `EOF` 발생 시 안전 종료
- 데이터 파일 손상 시 기본 데이터 복구

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
            "answer": 1
        }
    ],
    "best_score": {
        "points": 80,
        "correct_count": 4,
        "total_questions": 5
    }
}
```

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
