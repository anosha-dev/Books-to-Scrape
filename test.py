from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import math

driver = webdriver.Chrome()
 


books_data = []

# Keep scraping until there are no more pages

URL = "https://books.toscrape.com/"
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



        book_info = {
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock,
            "detail_page":detailed_url2
        }
        
        
        books_data.append(book_info)  

for book_info in books_data:
        URL = book_info["detail_page"]
        driver.get(URL)
    

        description = driver.find_element(By.XPATH, "//div[@id='product_description']/following-sibling::p").text
        UPC = driver.find_element(By.XPATH, "//th[text()='UPC']/following-sibling::td").text
        Product_type = driver.find_element(By.XPATH, "//th[text()='Product Type']/following-sibling::td").text
        Price_excluded_tax = driver.find_element(By.XPATH, "//th[text()='Price (excl. tax)']/following-sibling::td").text
        Price_included_tax= driver.find_element(By.XPATH, "//th[text()='Price (incl. tax)']/following-sibling::td").text 
        tax = driver.find_element(By.XPATH, "//th[text()='Tax']/following-sibling::td").text 
        availability = driver.find_element(By.XPATH, "//th[text()='Availability']/following-sibling::td").text
        reviews = driver.find_element(By.XPATH, "//th[text()='Number of reviews']/following-sibling::td").text 

        book_info["Description"] = description
        book_info["UPC"] = UPC 
        book_info["Product Type"] = Product_type
        book_info["Price Excluded Tax"] = Price_excluded_tax
        book_info["Price Included tax"] = Price_included_tax
        book_info["Tax"] = tax
        book_info["Availability"] = availability
        book_info["Reviews"] = reviews
                
        

       
print(books_data)

# Close the browser
driver.quit()


