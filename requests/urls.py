from django.urls import path   
from requests import views

requests_urlspatterns = [
    path('list/', views.solicitud_list, name='solicitud_list'),
]