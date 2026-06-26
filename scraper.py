from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()

driver.get("https://books.toscrape.com/")

books = driver.find_elements(By.CLASS_NAME, "product_pod")

books_data = []

for book in books:
   title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
   price = book.find_element(By.CLASS_NAME, "price_color").text
   rating =book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").replace("star-rating ", "")
   stock = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
   
   book_info = {"Title":title, "Price":price, "Rating":rating, "Stock":stock}
   books_data.append(book_info)

for book in books_data:
   print(f"Title:{book['Title']}")
   print(f"Price:{book['Price']}")
   print(f"Rating:{book['Rating']}")
   print(f"Stock:{book['Stock']}")
   print("-" * 40)

df = pd.DataFrame(books_data)
df.to_csv("books.csv", index=False)
print("Data saved successfully!")
driver.quit()