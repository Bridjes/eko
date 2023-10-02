from django.urls import path
from .views import index, add_solution

urlpatterns = [
    # запросы на страницы сайта
    path('', index),
    path('addsolution/', add_solution),
]