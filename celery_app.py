from celery import Celery

app = Celery('books_scraper', broker = 'redis://redis:6379/0' , backend = 'redis://redis:6379/0' ,include=['tasks'])