from django.shortcuts import render
from .models import Post, Category
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all()  # Список постов
    category = Category.objects.all()
    return render(request, 'index.html', {"posts": posts, 'category': category})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)  # Один пост
    return render(request, 'post_detail.html', {'post': post})

def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)  # Одна категория
    return render(request, 'category_detail.html', {'category': category})

def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'search_obj': search_obj})
