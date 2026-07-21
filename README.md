# Books-to-Scrape

A web scraping application built with **Python**, **Selenium**, **Celery**, **Redis**, **PostgreSQL**, and **Docker**.

The application scrapes book information from the **Books to Scrape** website and stores the extracted data in a PostgreSQL database. Celery executes scraping tasks asynchronously while Redis serves as the message broker.

---

## Features

- Scrapes book data from https://books.toscrape.com/
- Extracts:
  - Book ID
  - Title
  - Price
  - Rating
  - Stock Status
  - Product Description
  - UPC
  - Product Type
  - Price (Excluding Tax)
  - Price (Including Tax)
  - Tax
  - Availability
  - Number of Reviews
- Stores scraped data in PostgreSQL
- Uses Celery for asynchronous task execution
- Uses Redis as the message broker
- Runs using Docker and Docker Compose

---

## Technologies Used

- Python
- Selenium
- PostgreSQL
- SQLAlchemy
- Celery
- Redis
- Docker
- Docker Compose

---

## Project Structure

```text
Books-to-Scrape/
│
├── app/
│   ├── __init__.py
│   ├── celery_app.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── scraper.py
│   └── tasks.py
│
├── sql/
│   └── schema.sql
│
├── tests/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Getting Started

Run the application using Docker Compose.

```bash
docker compose up --build
```

---

## Database

The PostgreSQL database schema is initialized using:

```text
sql/schema.sql
```

---

## Workflow

1. `main.py` creates scraping tasks.
2. Redis queues the tasks.
3. Celery workers execute the tasks.
4. Selenium scrapes book information.
5. The scraped data is stored in PostgreSQL.

---

## Author

**Anosha**