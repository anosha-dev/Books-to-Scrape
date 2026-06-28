from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import math

load_dotenv()

# ---- Database Connection ----

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

row = pd.read_sql("SELECT COUNT(id) FROM books", engine)
row_no = row["count"][0]
page_no = math.floor (row_no / 20)
print(page_no)

# Open Chrome browser
driver = webdriver.Chrome()

# Starting page of the website
if page_no == 0:
    URL = "https://books.toscrape.com/"
    starting_url = "https://books.toscrape.com/"
else:
    URL = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
    starting_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"

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
        
        if URL == starting_url:

            title = title.replace("'", "")
            book_query = f"SELECT COUNT(*) FROM books WHERE title = '{title}'"
            book_result = pd.read_sql(book_query, engine)

            book_count = book_result["count"][0]

            if book_count > 0:
               continue
            else:
               books_data.append(book_info)
        
        else:
               books_data.append(book_info)


    
    if books_data:
      df = pd.DataFrame(books_data)
      df.to_sql("books", engine, if_exists="append", index=False)
      print("Data saved successfully!")
      books_data.clear()
    

    # Try to go to the next page
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        URL = next_button.get_attribute("href")

    # Stop the loop if there is no next page
    except:
        break



# Close the browser
driver.quit()


