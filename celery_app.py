from celery import Celery

app = Celery('books_scraper', broker = 'redis://localhost:6379/0' , backend = 'redis://localhost:6379/0' ,include=['tasks'])