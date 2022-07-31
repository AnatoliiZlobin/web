from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>Hello, World!</h1>')
    return render(request, 'blog/index.html')

def get_category(request, slug):
    return render(request, 'blog/category.html')
