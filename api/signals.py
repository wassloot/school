import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from models import User
from tasks import send_welcome_message, log_high_usage, send_booking_notification
from dotenv import load_dotenv


load_dotenv()

TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
TG_CHAT_ID = os.environ.get('TG_CHAT_ID')


@receiver(post_save, sender=User)
def send_welcome(instance, created):
    if created:
        send_welcome_message.delay(instance.id)


def room_usage_checker(room_id):
    if room_id == 1:
        log_high_usage.delay(room_id)


def booking_notification(booking_id):
    send_booking_notification.delay(booking_id)
