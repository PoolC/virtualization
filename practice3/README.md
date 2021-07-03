# 상황 3

## 배우고자 하는 것

- 도커를 이용하여 배포해보자
- 상황2(PM에 직접 배포) 와 상황3(도커를 이용한 배포)을 비교해보자 

## 상황

1. 서버 접속해서 프로비저닝하는게 귀찮아졌다
2. 라이브러리 설치와 같은 과정이 따분하게 느껴진다
3. python2, python3 를 계속 신경쓰는게 싫어졌다
4. 상황1에서 느낀 환경 분리의 이점을 docker를 통해 또 느껴보자

## 상황 재현

```bash
cp .Dockerfile Dockerfile
cp .Dockerfile_legacy Dockerfile_legacy

docker build -f .Dockerfile_legacy -t 도커허브아이디/py2:v1.0 .
docker run --rm --name legacy -p PORT1:8080 -d 도커허브아이디/py2:v1.0
docker ps

docker build -f .Dockerfile_legacy -t 도커허브아이디/py3:v1.0 .
docker run --rm --name main -p PORT2:8080 -d 도커허브아이디/py3:v1.0
docker ps

docker stop main legacy
```

이후 해설은 강의자료 참고
