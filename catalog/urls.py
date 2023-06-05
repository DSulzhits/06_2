from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', product, name='product')
]
