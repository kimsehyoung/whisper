FROM python:3.11.6

ENV TZ=Asia/Seoul

WORKDIR /home

COPY app/ .
COPY requirements.txt .

RUN apt update -y && apt install ffmpeg -y
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]