import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from celery_app import app
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

@app.task
def scrape(start_page, end_page): 
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium"

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    books_data = []

    while True:
        driver.get(start_page)
        books = driver.find_elements(By.CLASS_NAME, "product_pod")

        for book in books:
            title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            price = book.find_element(By.CLASS_NAME, "price_color").text
            rating = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").replace("star-rating ", "")
            stock = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
            detailed_url1 = book.find_element(By.CLASS_NAME, "image_container")
            detailed_url2 = detailed_url1.find_element(By.TAG_NAME, "a").get_attribute("href")

            id = detailed_url2.split("_")
            id = id[1]
            id = id.split("/")
            id = id[0]
            id = int(id)

            if stock == "In stock":
                stock = True
            else:
                stock = False

            price = float(price[1:])
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_map[rating]

            book_info = {
                "id": id,
                "title": title,
                "price": price,
                "rating": rating,
                "stock": stock,
                "detail_page": detailed_url2
            }
            books_data.append(book_info)

        for book_info in books_data:
            Detailed_URL = book_info["detail_page"]
            driver.get(Detailed_URL)

            try:
                description = driver.find_element(By.XPATH, "//div[@id='product_description']/following-sibling::p").text
            except:
                description = ""

            upc = driver.find_element(By.XPATH, "//th[text()='UPC']/following-sibling::td").text
            product_type = driver.find_element(By.XPATH, "//th[text()='Product Type']/following-sibling::td").text
            price_excluded_tax = driver.find_element(By.XPATH, "//th[text()='Price (excl. tax)']/following-sibling::td").text
            price_included_tax = driver.find_element(By.XPATH, "//th[text()='Price (incl. tax)']/following-sibling::td").text
            tax = driver.find_element(By.XPATH, "//th[text()='Tax']/following-sibling::td").text
            availability = driver.find_element(By.XPATH, "//th[text()='Availability']/following-sibling::td").text
            reviews = driver.find_element(By.XPATH, "//th[text()='Number of reviews']/following-sibling::td").text

            book_info["description"] = description
            book_info["upc"] = upc
            book_info["product_type"] = product_type
            book_info["price_excluded_tax"] = price_excluded_tax
            book_info["price_included_tax"] = price_included_tax
            book_info["tax"] = tax
            book_info["availability"] = availability
            book_info["reviews"] = reviews
            del book_info["detail_page"]

        if books_data:
            with engine.connect() as conn:
                for book in books_data:
                    conn.execute(text(
                        "INSERT INTO books (id, title, price, rating, stock, description, upc, product_type, "
                        "price_excluded_tax, price_included_tax, tax, availability, reviews) "
                        "VALUES (:id, :title, :price, :rating, :stock, :description, :upc, :product_type, "
                        ":price_excluded_tax, :price_included_tax, :tax, :availability, :reviews) "
                        "ON CONFLICT (id) DO NOTHING"
                    ), book)
                conn.commit()
            print("Data saved successfully!")
            books_data.clear()

        if start_page == end_page:
            break
        else:
            try:
                driver.get(start_page)
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
                start_page = next_button.get_attribute("href")
            except:
                break

    driver.quit()