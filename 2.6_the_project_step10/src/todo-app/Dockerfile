FROM oven/bun:1 AS frontend-base

WORKDIR /app

COPY frontend/package.json .

RUN bun install

COPY frontend/ .

RUN bun run build

FROM python:3.12-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install -r requirements.txt

COPY --from=frontend-base /app/dist ./dist

COPY backend/ .

ENV PORT=80

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
