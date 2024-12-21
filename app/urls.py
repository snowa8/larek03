from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/detail/<int:pk>/', views.category_detail, name='category_detail'),

    path('products/', views.product_list, name='product_list'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/detail/<int:pk>/', views.customer_detail, name='customer_detail'),
]
