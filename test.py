from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = "https://books.toscrape.com/"

driver.get(URL)

books = driver.find_elements(By.CLASS_NAME, "product_pod")


book = books[0]

title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
print(title)

price = book.find_element(By.CLASS_NAME, "price_color").text
print(price)

stock = book.find_element(By.CLASS_NAME, "availability").text
print(stock)

rating = book.find_element(By.CLASS_NAME,"star-rating").get_attribute("class").split()[1]
print(rating)