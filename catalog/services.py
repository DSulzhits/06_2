from django.core.mail import send_mail
from django.conf import settings


def send_email(record_object):
    send_mail(
        f'100 просмотров {record_object}',
        f'Юху! Уже 100 просмотров записи {record_object}!',
        settings.EMAIL_HOST_USER,
        recipient_list=['dsulzhits@gmail.com', 'suz17@bk.ru']
    )
