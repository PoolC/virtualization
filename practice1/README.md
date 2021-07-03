# 상황 1

## 배우고자 하는 것

- pyenv, conda, virtualenv 등을 이용하여 호스트와 분리된 파이썬 환경을 가상화하는 이유

## 상황

1. 약 10년 전에 작성한 코드를 바꾸기에는 너무 시간이 많이 들 것 같다
2. 최신 코드는 python3 으로 따로 실행되고 있다
3. 우리는 같은 컴퓨터에서 python2 로 legacy(기존에 작성한 코드)인 **main.py** 를 실행시키고 싶다

## 상황 재현 

```bash
brew link python  # python3 설치
python -m http.server YOUR_PORT &
ps aux | grep python  # python3 가 최신 코드를 따로 실행시키고 있다

python2 main.py YOUR_NAME
```

## 문제

```bash
python --version
python2 --version
```

- `python` 은 python3 이고 `python2` 는 python2 이다
- **collision.py** 에 있는 shebang(`#!/usr/bin/python`) 이 내부적으로 python3 로 바꿔버렸다

자세한 내용은 강의자료 참고

## 해결방법

```bash
pip install virtualenv
virtualenv py2env --python=python2
source py2env/bin/activate

python --version
python main.py
```
