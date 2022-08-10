from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
def all_blogs(reguest):

    blogs = Blog.objects.order_by('-date')

    return render(reguest, 'blog/all_blogs.html',{'blogs': blogs})
def detail(reguest,blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(reguest, 'blog/detail.html', {'blog':blog})