from celery import Celery

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery("background_tasks", broker="redis://localhost:6379")
