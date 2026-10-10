from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.detail, name='detail'),
    path('sell/', views.add_product, name='add_product'),
    path('sell/mine/', views.my_products, name='my_products'),
]
