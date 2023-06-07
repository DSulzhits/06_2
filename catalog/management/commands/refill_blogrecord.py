from django.core.management import BaseCommand
from catalog.models import BlogRecord


class Command(BaseCommand):
    def handle(self, *args, **options):
        BlogRecord.objects.all().delete()
        category_list = [{
            "title": "Бот",
            "slug": "Бот",
            "content": "Бот, а также интернет-бот — виртуальный робот или искусственный интеллект, который функционирует на основе специальной программы, выполняющий автоматически и/или по заданному расписанию какие-либо действия через интерфейсы, предназначенные для людей.",
            "preview": "images/tg_bot.jpg",
            "created": "",
            "sign_of_publication": True,
            "views": 0
        },
            {
                "title": "Рассылка",
                "slug": "Рассылка",
                "content": "Рассылка — это отправка одного уведомления большому количеству получателей. Это может быть email, SMS, push рассылка, рассылка в мессенджеры и социальные сети. Обычно она осуществляется через сервис рассылок. Можно комбинировать эти виды рассылок для лучшей эффективности.",
                "preview": "images/mailing_list.png",
                "created": "",
                "sign_of_publication": True,
                "views": 0
            },
            {
                "title": "Утилита",
                "slug": "Утилита",
                "content": "Утилита - вспомогательная компьютерная программа в составе общего программного обеспечения для выполнения специализированных типовых задач, связанных с работой оборудования и операционной системы.",
                "preview": "images/utility.jpg",
                "created": "",
                "sign_of_publication": True,
                "views": 0
            },
            {
                "title": "Веб-Приложение",
                "slug": "Веб-Приложение",
                "content": "Веб-приложение — клиент-серверное приложение, в котором клиент взаимодействует с веб-сервером при помощи браузера. Логика веб-приложения распределена между сервером и клиентом, хранение данных осуществляется, преимущественно, на сервере, обмен информацией происходит по сети.",
                "preview": "images/web-app.jpg",
                "created": "",
                "sign_of_publication": True,
                "views": 0
            },
        ]

        category_objects = []

        for category_item in category_list:
            category_objects.append(BlogRecord(**category_item))

        BlogRecord.objects.bulk_create(category_objects)
