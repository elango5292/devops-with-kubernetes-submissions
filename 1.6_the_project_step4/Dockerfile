FROM oven/bun:1 AS frontend-base

WORKDIR /app

COPY src/frontend/package.json .

RUN bun install

COPY src/frontend/ .

RUN bun run build

FROM python:3.12-slim

WORKDIR /app

COPY src/backend/requirements.txt .

RUN pip install -r requirements.txt

COPY --from=frontend-base /app/dist ./dist

COPY src/backend/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
