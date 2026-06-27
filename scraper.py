from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# ---- Database Connection ----

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
# Open Chrome browser
driver = webdriver.Chrome()

# Starting page of the website
URL = "https://books.toscrape.com/"

books_data = []

# Keep scraping until there are no more pages
while True:
    
    driver.get(URL)

    # Find all books on the page
    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    # Get information from each book
    for book in books:

        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.CLASS_NAME, "price_color").text
        rating = book.find_element( By.CLASS_NAME, "star-rating").get_attribute("class").replace("star-rating ", "")
        stock = book.find_element(By.CSS_SELECTOR, "p.instock.availability"  ).text.strip()
        
        if stock == "In stock":
          stock = True
        else:
          stock = False


        price = price[1:]
        price = float(price)


        rating_map={"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
        rating = rating_map[rating] 


        book_info = {
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock
        }

        books_data.append(book_info)

    # Try to go to the next page
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        URL = next_button.get_attribute("href")

    # Stop the loop if there is no next page
    except:
        break

# Convert the list into a DataFrame
df = pd.DataFrame(books_data)


# ---- Save to PostgreSQL ----
df.to_sql("books", engine, if_exists="append", index=False)

print("Data saved successfully!")

# Close the browser
driver.quit()


