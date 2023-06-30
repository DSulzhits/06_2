from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView, ProductDeleteView, \
    ProductCreateView, \
    ProductUpdateView, BlogRecordListView, \
    BlogRecordDetailView, BlogRecordCreateView, BlogRecordUpdateView, BlogRecordDeleteView, \
    BlogRecordDeactivatedListView, toggle_activity, VersionDetailView, VersionListView, VersionCreateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('version/create/', never_cache(VersionCreateView.as_view()), name='version_create'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('blog_records/', BlogRecordListView.as_view(), name='blog_records'),
    path('blog_records_deactivated/', BlogRecordDeactivatedListView.as_view(), name='blog_records_deactivated'),
    path('blog_records/<slug:slug>/', BlogRecordDetailView.as_view(), name='blog_record_detail'),
    path('blog_record/create/', never_cache(BlogRecordCreateView.as_view()), name='blog_record_create'),
    path('blog_record/update/<slug:slug>/', never_cache(BlogRecordUpdateView.as_view()), name='blog_record_update'),
    path('blog_record/delete/<slug:slug>/', never_cache(BlogRecordDeleteView.as_view()), name='blog_record_delete'),
    path('blog_record/toggle/<slug:slug>/', toggle_activity, name='toggle_activity'),
]
