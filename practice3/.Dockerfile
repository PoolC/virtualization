FROM python:3.9.6-slim

WORKDIR /usr/src/app

COPY requirements_py3.txt .
COPY server_py3.py .

RUN pip install -r requirements_py3.txt

ENTRYPOINT ["python", "server_py3.py", "EMPTY_NAME ):", "8080"]
