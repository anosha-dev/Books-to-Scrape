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


