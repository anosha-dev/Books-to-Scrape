from .tasks import scrape

for i in range(1,51,10):
    start_page = f"https://books.toscrape.com/catalogue/page-{i}.html"
    end_page = f"https://books.toscrape.com/catalogue/page-{i+9}.html"

    scrape.delay(start_page, end_page)
   