FROM python:3.14

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY app/ app/

COPY .env .

CMD ["python", "-m", "celery", "-A", "app.celery_app", "worker", "--loglevel=info"]