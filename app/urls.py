from django.urls import path
from .views import index, category_detail, search_result, post_detail

urlpatterns = [
    path('uz/', index, name='index'),  # Определяем маршрут для базового представления
    path('category/<slug:slug>/', category_detail,name='category_detail_url'),
    path('post/<slug:slug>/', post_detail ,name='post_detail_url'),
    path('search/', search_result, name='search_result'),
]