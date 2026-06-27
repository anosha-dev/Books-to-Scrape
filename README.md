# Books-to-Scrape

A Selenium-based web scraper for the [Books to Scrape](https://books.toscrape.com/) website.

## Description

This project is built using Python and Selenium. It scrapes book data from all pages of the Books to Scrape website and stores it in a PostgreSQL database.

## Data Collected

- Title
- Price
- Rating
- Stock

## Requirements

- Python 3
- Selenium
- Pandas
- SQLAlchemy
- psycopg2
- Google Chrome
- PostgreSQL

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Configure the database

- Install PostgreSQL from https://postgresql.org
- Open pgAdmin and run `schema.sql` in the Query Tool to create the database and table

### 2. Set up environment variables

Copy `.env.example` to `.env` and fill in your PostgreSQL credentials:

```env
DB_HOST=localhost
DB_NAME=scraper_db
DB_USER=postgres
DB_PASSWORD=......
DB_PORT=5432
```

## How to Run

Activate your virtual environment first:

```bash
venv\Scripts\activate
```

Then run the scraper:

```bash
python scraper.py
```

Once finished, all 1000 books will be saved to the `books` table in your PostgreSQL database.

## Website

https://books.toscrape.com/

## Author

Anosha