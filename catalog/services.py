from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from catalog.models import Category


def send_email(record_object):
    send_mail(
        f'100 просмотров {record_object}',
        f'Юху! Уже 100 просмотров записи {record_object}!',
        settings.EMAIL_HOST_USER,
        recipient_list=['dsulzhits@gmail.com', 'suz17@bk.ru']
    )


def get_cached_category_subjects():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
