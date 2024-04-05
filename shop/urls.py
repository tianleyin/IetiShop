from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list),
    path('cat/<int:categoria_id>/', views.product_list, name='product_list'),
    path('prod/<int:producto_id>/', views.product_detail, name='product_detail'),
]
