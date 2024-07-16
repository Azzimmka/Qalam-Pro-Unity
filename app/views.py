from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def index(request):
    post = Post.objects.order_by('date_pub')[:1]
    category = Category.objects.all()
    return render(request, 'index.html', {"post": post, 'category': category})