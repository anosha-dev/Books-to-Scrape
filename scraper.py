from selenium import webdriver

# Launch Chrome
driver = webdriver.Chrome()

# Open the website
driver.get("https://books.toscrape.com/")

# Print the page title
print(driver.title)

# Keep the browser open for 5 seconds
import time
time.sleep(5)

# Close the browser
driver.quit()