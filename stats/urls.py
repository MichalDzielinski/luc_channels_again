from django.urls import path
from . import views

app_name='stats'

urlpatterns = [
    path('', views.main, name='main'),
    path('<slug>', views.dashboard, name='dashboard'),
    path('<slug>/chart/', views.chat_data, name='chart'),
]