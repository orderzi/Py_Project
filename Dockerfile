FROM python:3.8-slim-buster

WORKDIR /app

ENV DB_USER=root

ENV DB_PASSWORD=root

ENV DB_HOST=localhost

ENV DB_DATABASE=flaskdb

ENV FLASK_URL=http://changeme.com/scores

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5001

CMD python3 Main_Scores.py
