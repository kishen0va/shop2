from time import sleep
from clothes.celery import app
from .models import RSSSubs
from .bot import send_message_to_all_users_by_telegram


@app.task
def add_two_numbers(a: int, b: int) -> int:
    sleep(5)
    return a + b


@app.task
def send_message_to_user_tg_task():
    message = 'Привет, на эти выходные есть супер скидки на одежду'
    users = RSSSubs.objects.all().values_list('id', flat=True)
    send_message_to_all_users_by_telegram(message,  users)

