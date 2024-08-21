from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_main,name='clients_main'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('list/', views.list, name='list'),
    path('stuff/', views.stuff, name='stuff')
]