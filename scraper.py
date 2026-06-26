from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

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
            
        book_info = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Stock": stock
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

# Save the data into a CSV file
df.to_csv("books.csv", index=False)

print("Data saved successfully!")

# Close the browser
driver.quit()