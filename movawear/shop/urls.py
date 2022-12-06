from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ShopHomeView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('register/', register, name='register'),
    path('delivery/', delivery, name='delivery'),
    path('product/<slug:product_slug>', ShowProductView.as_view(), name='product'),
    path('category/<slug:catalog_slug>', ShowCategoryView.as_view(), name='category'),
    re_path(r'example/(?P<example_flag>[0-9]{4})/', example, name='example'),
    #как использовать модуль ре в джанго
]
