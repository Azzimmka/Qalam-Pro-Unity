from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def index(request):
    post = Post.objects.all()   #order_by('date_pub')[:1]
    category = Category.objects.all()
    return render(request, 'index.html', {"post": post, 'category': category})


def category_detail(request, slug):
    categories = Category.objects.get(slug__iexact=slug)
    return render(request,'category_detail.html',{'categories':categories})