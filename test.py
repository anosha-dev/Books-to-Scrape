from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
URL = "https://books.toscrape.com/"
driver.get(URL)

books_data = []

books = driver.find_elements(By.CLASS_NAME, "product_pod")

book = books[0]

title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
print(title)

detailed_url = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")
print(detailed_url)

price = book.find_element(By.CLASS_NAME, "price_color").text
print(price)

stock = book.find_element(By.CLASS_NAME, "availability").text
print(stock)

rating = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()[1]
print(rating)



driver.get(detailed_url)

description = driver.find_element(By.XPATH, "//div[@id='product_description']/following-sibling::p").text
print(description)

UPC = driver.find_element(By.XPATH, "//th[text()='UPC']/following-sibling::td").text
print(UPC)

product_type = driver.find_element(By.XPATH, "//th[text()='Product Type']/following-sibling::td").text
print(product_type)

Price_excl_tax = driver.find_element(By.XPATH, "//th[text()='Price (excl. tax)']/following-sibling::td").text
print(Price_excl_tax)

Price_incl_tax = driver.find_element(By.XPATH, "//th[text()='Price (incl. tax)']/following-sibling::td").text
print(Price_incl_tax)

tax = driver.find_element(By.XPATH, "//th[text()='Tax']/following-sibling::td").text
print(tax)

availability = driver.find_element(By.XPATH, "//th[text()='Availability']/following-sibling::td").text.split("(")[1]
availability = availability.split(" ")[0]
print(availability)

reviews = driver.find_element(By.XPATH, "//th[text()='Number of reviews']/following-sibling::td").text
print(reviews)





