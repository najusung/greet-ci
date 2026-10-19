# greet-ci

명령행 인수로 받은 이름에 인사하는 프로그램과 GitHub Actions CI 예제.

## 설치

```bash
uv lock
```

## 실행

```bash
uv run --locked python greet.py Hee
uv run --locked python greet.py
```

## 검사

```bash
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
uv build
```
