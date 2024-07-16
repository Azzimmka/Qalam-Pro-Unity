from django.urls import path
from .views import index

urlpatterns = [
    path('uz', index, name='index'),  # Определяем маршрут для базового представления
]