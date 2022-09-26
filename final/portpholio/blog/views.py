from django.shortcuts import render
from django.http import HttpResponse
from math import ceil as ccc
from .models import Blog,Education

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev=page-1
    else:
        prev = None
    if page < ccc(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'blog/blog.html', context)

def blogpost(request, slug):
    longblogs = Blog.objects.filter(slug=slug).first()
    longblogslist = {'name': longblogs}
    return render(request, 'blog/blogpost.html', longblogslist)

def edu(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Education.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page>1:
        prev=page-1
    else:
        prev = None
    if page < ccc(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'blog/blog_edu.html', context)

def blogpost_edu(request, slug):
    longblogs = Education.objects.filter(slug=slug).first()
    longblogslist = {'name': longblogs}
    return render(request, 'blog/blogpost_edu.html', longblogslist)

def contact(request):
    return render(request, 'blog/contact.html')

def search(request):
    a = (request.GET.get("slug"))
    longblogs = Blog.objects.filter(slug=a).first()
    print(longblogs)
    longblogslist = {'name': longblogs}
    return render(request, 'blog/blogpost.html', longblogslist)
