FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y gcc \
    apt-get install -y ffmpeg


COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
