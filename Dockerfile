FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

ENV DB_USER=root

ENV DB_PASSWORD=root

ENV DB_HOST=localhost

ENV DB_DATABASE=flaskdb

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

CMD python3 Main_Scores.py
