CREATE DATABASE scrapper_db;

\c scraper_db

DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(500),
    price NUMERIC,
    rating INTEGER,
    stock BOOLEAN,
    description TEXT,
    upc VARCHAR(50),
    product_type VARCHAR(50),
    price_excluded_tax VARCHAR(20),
    price_included_tax VARCHAR(20),
    tax VARCHAR(20),
    availability VARCHAR(50),
    reviews INTEGER,
    scraped_at TIMESTAMP DEFAULT NOW()
);