from django.urls import path
from . import views
urlpatterns = [
    path('mine/', views.my_orders, name='my_orders'),
    path('incoming/', views.incoming, name='incoming_orders'),
    path('<int:pk>/status/', views.update_status, name='update_status'),
]
