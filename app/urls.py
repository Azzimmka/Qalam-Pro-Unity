from django.urls import path
from .views import index, category_detail

urlpatterns = [
    path('uz', index, name='index'),  # Определяем маршрут для базового представления
    path('category/<slug:slug>/', category_detail,name='category_detail_url'),
]