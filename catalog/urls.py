from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView, BlogRecordListView, \
    BlogRecordDetailView, BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog_records/', BlogRecordListView.as_view(), name='blog_records'),
    path('blog_records/<slug:slug>/', BlogRecordDetailView.as_view(), name='blog_record_detail'),
    path('blog_record/create/', BlogRecordCreateView.as_view(), name='blog_record_create'),
    path('blog_record/update/<int:pk>/', BlogRecordUpdateView.as_view(), name='blog_record_update'),
    path('blog_record/delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='blog_record_delete'),
]
