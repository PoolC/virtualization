# 상황 2

## 배우고자 하는 것

- 서버에 직접 provisioning 을 해보자 (PM 에 직접 배포)
- python2, python3 로 각각 서버를 띄워보자

## 상황

1. 서버 발주하고 OS까지 설치 된 상태로 전달받았다
2. python이나 기타 필요한 패키지는 내가 설치해야한다

## 상황 재현

```bash
brew link python

# python2 서버 실행
python2 -m SimpleHTTPServer PORT1 &

# python3 서버 실행
pip install -r requirements_py3.txt
python server_py3.py YOUR_NAME PORT2 &
```
