# Books-to-Scrape
<<<<<<< HEAD

A Selenium-based web scraper for the [Books to Scrape](https://books.toscrape.com/) website.

## Description

This project is built using Python and Selenium. It scrapes book data from all pages of the Books to Scrape website and stores it in a PostgreSQL database.
=======
Selenium-based web scraper for Books to Scrape website.

## Description

This project is made using Python and Selenium.

It visits the **Books to Scrape** website, collects book information from every page, and saves the data into a CSV file.
>>>>>>> de7820acd3064d27994433773ae32fa205a30830

## Data Collected

- Title
- Price
- Rating
- Stock

## Requirements

- Python 3
- Selenium
- Pandas
<<<<<<< HEAD
- SQLAlchemy
- psycopg2
- Google Chrome
- PostgreSQL
=======
- Google Chrome
>>>>>>> de7820acd3064d27994433773ae32fa205a30830

Install the required libraries:

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
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
=======
## How to Run

Run the following command:
>>>>>>> de7820acd3064d27994433773ae32fa205a30830

```bash
python scraper.py
```

<<<<<<< HEAD
Once finished, all 1000 books will be saved to the `books` table in your PostgreSQL database.
=======
After the program finishes, a file named `books.csv` will be created.
>>>>>>> de7820acd3064d27994433773ae32fa205a30830

## Website

https://books.toscrape.com/
<<<<<<< HEAD

## Author

Anosha
=======
>>>>>>> de7820acd3064d27994433773ae32fa205a30830
