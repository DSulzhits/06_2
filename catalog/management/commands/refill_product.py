from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        category_list = [{
            "name": "E-mail рассылка",
            "description": "Отправка ваших уведомлений на почту сотрудников",
            "image": "images/mailing_list.png",
            "category": Category.objects.get(name="рассылки"),
            "price": 10000,
            "created": "",
            "updated": "",
        },
            {
                "name": "Бот поддержки",
                "description": "Бот который позволяет понять проблему клиента, и направить его к нужному специалисту",
                "image": "images/tg_bot.jpg",
                "category": Category.objects.get(name="Телеграм боты"),
                "price": 8000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Диагностика ПО",
                "description": "Утилита для диагностики состояния вашего ПО и выявления возможных ошибок",
                "image": "images/diagnostic_1.jpg",
                "category": Category.objects.get(name="Полезные утилиты"),
                "price": 20000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Sky-Cloud",
                "description": "Облачное хранилище для надежного размещения ваших данных",
                "image": "images/web-app.jpg",
                "category": Category.objects.get(name="Веб-приложения"),
                "price": 1000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Бот рассылки",
                "description": "Бот который рассылает ваши уведомления в телеграм чаты и группы",
                "image": "images/msg_bot.jpg",
                "category": Category.objects.get(name="Телеграм боты"),
                "price": 12000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Sky-Security",
                "description": "Утилита для защиты вашего устройства от вредоносного ПО и злоумышленников",
                "image": "images/security.png",
                "category": Category.objects.get(name="Полезные утилиты"),
                "price": 5000,
                "created": "",
                "updated": "",
            },
            {
                "name": "Sky-Mail",
                "description": "Ваш собственный почтовый сервер, на базе нашего облачного хранилища",
                "image": "images/mail.jpg",
                "category": Category.objects.get(name="Веб-приложения"),
                "price": 30000,
                "created": "",
                "updated": "",
            },
        ]

        category_objects = []

        for category_item in category_list:
            category_objects.append(Product(**category_item))

        Product.objects.bulk_create(category_objects)
