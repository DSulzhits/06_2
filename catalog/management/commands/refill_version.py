from django.core.management import BaseCommand
from catalog.models import Version, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Version.objects.all().delete()
        version_list = [{
            "product": Product.objects.get(name="E-mail рассылка"),
            "number": "1",
            "name": f"{Product.objects.get(name='E-mail рассылка').name} 1",
            "sign_of_current_version": True,
        },
            {
                "product": Product.objects.get(name="Бот поддержки"),
                "number": "3",
                "name": f"{Product.objects.get(name='Бот поддержки').name} 3",
                "sign_of_current_version": True,
            },
            {
                "product": Product.objects.get(name="Диагностика ПО"),
                "number": "2",
                "name": f"{Product.objects.get(name='Диагностика ПО').name} 2",
                "sign_of_current_version": True,
            },
            {
                "product": Product.objects.get(name="Sky-Cloud"),
                "number": "5",
                "name": f"{Product.objects.get(name='Sky-Cloud').name} 5",
                "sign_of_current_version": True,
            },
            {
                "product": Product.objects.get(name="Бот рассылки"),
                "number": "1",
                "name": f"{Product.objects.get(name='Бот рассылки').name} 1",
                "sign_of_current_version": True,
            },
            {
                "product": Product.objects.get(name="Sky-Security"),
                "number": "1",
                "name": f"{Product.objects.get(name='Sky-Security').name} 1",
                "sign_of_current_version": True,
            },
            {
                "product": Product.objects.get(name="Sky-Mail"),
                "number": "1",
                "name": f"{Product.objects.get(name='Sky-Mail').name} 1",
                "sign_of_current_version": False,
            },

        ]

        version_objects = []

        for version_item in version_list:
            version_objects.append(Version(**version_item))

        Version.objects.bulk_create(version_objects)
