from .celery_app import app
from .database import insert_books
from .scraper import scrape_books


@app.task
def scrape(start_page, end_page):
    print(f"Starting scrape: {start_page} -> {end_page}")

    books_data = scrape_books(start_page, end_page)

    print(f"Scraped {len(books_data)} books")

    insert_books(books_data)

    print("Finished saving")