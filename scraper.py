import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import math
from sqlalchemy import create_engine, text

load_dotenv()

# ---- Database Connection ----

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

row = pd.read_sql("SELECT COUNT(id) FROM books", engine)
row_no = row["count"][0]
page_no = math.floor (row_no / 20)

if row_no != 0 and row_no % 20 == 0:
    page_no = page_no + 1

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

        detailed_url1 = book.find_element(By.CLASS_NAME, "image_container")
        detailed_url2= detailed_url1.find_element(By.TAG_NAME,"a").get_attribute("href")

        id = detailed_url2.split("_")
        id = id[1]
        id = id.split("/")
        id = id[0]
        id =int(id)
        
        if stock == "In stock":
          stock = True
        else:
          stock = False


        price = price[1:]
        price = float(price)


        rating_map={"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
        rating = rating_map[rating] 


        book_info = {
            "id" : id,
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock,
            "detail_page":detailed_url2
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

        price_included_tax= driver.find_element(By.XPATH, "//th[text()='Price (incl. tax)']/following-sibling::td").text 

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
            conn.execute(text("INSERT INTO books (id, title, price, rating, stock, description, upc, product_type, price_excluded_tax, price_included_tax, tax, availability, reviews) VALUES (:id, :title, :price, :rating, :stock, :description, :upc, :product_type, :price_excluded_tax, :price_included_tax, :tax, :availability, :reviews) ON CONFLICT (id) DO NOTHING"), book)
         conn.commit()

      print("Data saved successfully!")
      books_data.clear()
    

    # Try to go to the next page
    try:
        driver.get(URL)
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        URL = next_button.get_attribute("href")

    # Stop the loop if there is no next page
    except:
        break



# Close the browser
driver.quit()





