import os


import logging
from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv
from models import User, Room, Booking

load_dotenv()

TG_BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
TG_CHAT_ID = os.environ.get('TG_CHAT_ID')


@shared_task
def send_welcome_message(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        subject='Welcome',
        message=f'Hi {user.username}! Welcome to our flexible booking service',
        from_email='<EMAIL>',
        recipient_list=[user.email],
    )



@shared_task
def log_high_usage(room_id):
    room = Room.objects.get(id=room_id)
    logging.info(f'Room {room.name} has been used high.')



@shared_task
def send_booking_notification(booking_id):
    booking = Booking.objects.get(id=booking_id)
    send_mail(
        subject='Booking confrimation',
        message=f'Your booking has been confirmed. Your booking id is {booking.id}.',
        from_email='<EMAIL>',
        recipient_list=[booking.user.email],
    )







