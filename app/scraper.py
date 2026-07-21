from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def scrape_books(start_page, end_page):
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
            rating = (
                book.find_element(By.CLASS_NAME, "star-rating")
                .get_attribute("class")
                .replace("star-rating ", "")
            )
            stock = (
                book.find_element(By.CSS_SELECTOR, "p.instock.availability")
                .text.strip()
            )

            detail_page = (
                book.find_element(By.CLASS_NAME, "image_container")
                .find_element(By.TAG_NAME, "a")
                .get_attribute("href")
            )

            book_id = int(detail_page.split("_")[1].split("/")[0])

            rating_map = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5,
            }

            books_data.append(
                {
                    "id": book_id,
                    "title": title,
                    "price": float(price[1:]),
                    "rating": rating_map[rating],
                    "stock": stock == "In stock",
                    "detail_page": detail_page,
                }
            )
         
        
        for book in books_data:
            
            driver.get(book["detail_page"])
        
            try:
                description = driver.find_element(
                    By.XPATH,
                    "//div[@id='product_description']/following-sibling::p",
                ).text
            except:
                description = ""

            book["description"] = description
            book["upc"] = driver.find_element(
                By.XPATH,
                "//th[text()='UPC']/following-sibling::td",
            ).text
            book["product_type"] = driver.find_element(
                By.XPATH,
                "//th[text()='Product Type']/following-sibling::td",
            ).text
            book["price_excluded_tax"] = driver.find_element(
                By.XPATH,
                "//th[text()='Price (excl. tax)']/following-sibling::td",
            ).text
            book["price_included_tax"] = driver.find_element(
                By.XPATH,
                "//th[text()='Price (incl. tax)']/following-sibling::td",
            ).text
            book["tax"] = driver.find_element(
                By.XPATH,
                "//th[text()='Tax']/following-sibling::td",
            ).text
            book["availability"] = driver.find_element(
                By.XPATH,
                "//th[text()='Availability']/following-sibling::td",
            ).text
            book["reviews"] = driver.find_element(
                By.XPATH,
                "//th[text()='Number of reviews']/following-sibling::td",
            ).text

            

        if start_page == end_page:
            break

        try:
            driver.get(start_page)
            next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            start_page = next_button.get_attribute("href")
        except:
            break
    
    
    driver.quit()
    return books_data