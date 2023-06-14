from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [{
            "name": "рассылки",
            "description": "отправка одного уведомления большому количеству получателей"
        },
            {
                "name": "Телеграм боты",
                "description": "виртуальный робот или искусственный интеллект, который функционирует на основе специальной программы, выполняющий автоматически и/или по заданному расписанию какие-либо действия через интерфейсы, предназначенные для людей"
            },
            {
                "name": "Полезные утилиты",
                "description": "вспомогательная компьютерная программа в составе общего программного обеспечения для выполнения специализированных типовых задач"
            },
            {
                "name": "Веб-приложения",
                "description": "различные приложения для вашего браузера"
            }
        ]

        category_objects = []

        for category_item in category_list:
            category_objects.append(Category(**category_item))

        Category.objects.bulk_create(category_objects)
