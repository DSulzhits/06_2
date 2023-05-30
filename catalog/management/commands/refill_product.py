from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        category_list = [{
                "name": "Рассылка на электронную почту",
                "description": "Отправка ваших уведомлений на почту сотрудников",
                "image": "categories/mailing_list.jpg",
                "category": Category.objects.get(name="рассылки"),
                "price": 10000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Бот поддержки",
                "description": "Бот который позволяет понять проблему клиента, и направить его к нужному специалисту",
                "image": "categories/tg_bot.jpg",
                "category": Category.objects.get(name="Телеграм боты"),
                "price": 8000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Диагностика ПО",
                "description": "Утилита для диагностики состояния вашего ПО и выявления возможных ошибок",
                "image": "categories/diagnostic.jpg",
                "category": Category.objects.get(name="Полезные утилиты"),
                "price": 20000,
                "created": "",
                "updated": "",
            }]

        category_objects = []

        for category_item in category_list:
            category_objects.append(Product(**category_item))

        Product.objects.bulk_create(category_objects)
