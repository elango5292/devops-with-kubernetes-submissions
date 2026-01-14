FROM python:3.12-slim

WORKDIR /usr/src/app

ENV APP_PORT=8000

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE ${APP_PORT}

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}