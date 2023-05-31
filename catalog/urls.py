from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, info

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('info/', info)
]
