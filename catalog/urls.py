from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView, ProductDeleteView, \
    ProductCreateView, \
    ProductUpdateView, BlogRecordListView, \
    BlogRecordDetailView, BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView, \
    BlogRecordDeactivatedListView, toggle_activity, VersionDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='product_version'),
    path('blog_records/', BlogRecordListView.as_view(), name='blog_records'),
    path('blog_records_deactivated/', BlogRecordDeactivatedListView.as_view(), name='blog_records_deactivated'),
    path('blog_records/<slug:slug>/', BlogRecordDetailView.as_view(), name='blog_record_detail'),
    path('blog_record/create/', BlogRecordCreateView.as_view(), name='blog_record_create'),
    path('blog_record/update/<slug:slug>/', BlogRecordUpdateView.as_view(), name='blog_record_update'),
    path('blog_record/delete/<slug:slug>/', BlogRecordDeleteView.as_view(), name='blog_record_delete'),
    path('blog_record/toggle/<slug:slug>/', toggle_activity, name='toggle_activity'),
]
