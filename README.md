# Books to Scrape

A web scraping application built with Python that collects book information from [Books to Scrape](https://books.toscrape.com/) and stores it in a PostgreSQL database.

The application uses Selenium for scraping, Celery for asynchronous task processing, Redis as the message broker, and Docker Compose to run the application and its services in containers.

## Features

* Scrapes book information from the Books to Scrape website
* Extracts:

  * Book ID
  * Title
  * Price
  * Rating
  * Stock Status
  * Product Description
  * UPC
  * Product Type
  * Price excluding tax
  * Price including tax
  * Tax
  * Availability
  * Number of reviews
* Stores scraped data in PostgreSQL
* Processes scraping tasks asynchronously using Celery
* Uses Redis as the Celery message broker
* Runs the application using Docker and Docker Compose

## Tech Stack

* Python
* Selenium
* PostgreSQL
* SQLAlchemy
* Celery
* Redis
* Docker
* Docker Compose

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

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed.

### Clone the Repository

```bash
git clone https://github.com/anosha-dev/Books-to-Scrape.git
cd Books-to-Scrape
```

### Configure Environment Variables

Create a `.env` file using the provided example:

```bash
cp .env.example .env
```

Update the environment variables if needed.

### Run the Application

Build and start the containers:

```bash
docker compose up --build
```

## Workflow

1. `main.py` creates the scraping tasks.
2. Redis receives and queues the tasks.
3. Celery workers process the tasks asynchronously.
4. Selenium scrapes the book information.
5. The scraped data is stored in PostgreSQL.

## Database

The PostgreSQL database schema is initialized using:

```text
sql/schema.sql
```

## Author

**Anosha**

[GitHub Profile](https://github.com/anosha-dev)
