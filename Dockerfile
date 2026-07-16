FROM python:3.14

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


RUN pip install -r requirements.txt

COPY requirements.txt .
COPY celery_app.py .
COPY main.py .
COPY tasks.py .
COPY .env .

CMD ["python", "-m", "celery", "-A", "celery_app", "worker", "--loglevel=info"]