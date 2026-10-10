from django.urls import path
from django.contrib.auth import views as v
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', v.LoginView.as_view(template_name='form.html', extra_context={'title': 'Log in', 'button': 'Log in'}), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
]
