# Books-to-Scrape

A web scraper for the [Books to Scrape](https://books.toscrape.com/) website.

## Description

This project is built using Python and Selenium. It scrapes book data from all pages of the website and stores it in a PostgreSQL database.

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

```bash
pip install -r requirements.txt
```

## Setup

1. Install PostgreSQL and open pgAdmin
2. Run `schema.sql` in the Query Tool to create the table
3. Copy `.env.example` to `.env` and add your database credentials

## How to Run

```bash
python scraper.py
```

Data will be saved to the `books` table in your PostgreSQL database.

## Website

https://books.toscrape.com/

## Author

Anosha