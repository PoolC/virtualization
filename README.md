# 가상화 세미나

## 시작하기 전에

```bash
# local
ssh 유저명@poolc-pc.local

# remote
brew install git
```

## 명령어
### PM 배포

```bash
# remote
python legacy.py
brew link python
python3 main.py
```

### Docker 배포

```bash
# remote
brew install --cask docker

# local
git clone https://github.com/PoolC/virtualization
cd virtualization

vim Dockerfile
docker build -t 도커허브아이디/main:v1.0 .  # '.' 꼭 넣어주세요
docker run --rm --name main_test -d 도커허브아이디/main:v1.0
docker push 도커허브아이디/main:v1.0

vim Dockerfile_legacy
docker build -f Dockerfile_legacy -t 도커허브아이디/legacy:v1.0 .  # '.' 꼭 넣어주세요
docker run --rm --name legacy_test -d 도커허브아이디/legacy:v1.0
docker push 도커허브아이디/legacy:v1.0

# remote
docker run --rm --name legacy -d 도커허브아이디/legacy:v1.0
docker run --rm --name main -d 도커허브아이디/main:v1.0
```
