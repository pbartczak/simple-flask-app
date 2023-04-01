FROM python:3.9-slim-buster

WORKDIR /app

COPY ./flask-app/ .
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
