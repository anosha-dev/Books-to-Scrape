CREATE DATABASE scrapper_db;

\c scraper_db

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR (500),
    price VARCHAR (50),
    rating VARCHAR (20),
    stock VARCHAR  (50)
    scraped_at TIMESTAMP DEFAULT NOW()
);