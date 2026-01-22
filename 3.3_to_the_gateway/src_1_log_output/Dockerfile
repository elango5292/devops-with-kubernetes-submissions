FROM python:3.12-slim

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV APP_PORT=8000

EXPOSE ${APP_PORT}

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}