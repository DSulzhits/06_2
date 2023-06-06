from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]
