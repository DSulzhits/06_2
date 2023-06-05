from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]
