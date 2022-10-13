from multiprocessing import context
from turtle import right
from unittest import result
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Blog , Tag, Trader


def home(request):
    trader = Trader.objects.all()
    context = {"trader":trader}

    return render(request, 'home/home.html', context)


def Journal(request):

    blog = Blog.objects.all()
   


    page = request.GET.get('page')
    results = 3
    paginator = Paginator(blog, results)

    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        page=1
        blog = paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        blog = paginator.page(page)


    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5 )

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custome_range = range(leftIndex,rightIndex)




    


    context= {'blog': blog, 'paginator':paginator, 'custome_range':custome_range, }

    return render(request, 'home/journal.html', context)


def single(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    tags = blog.tags.all()

    context = {'blog':blog, 'tags':tags}

    return render(request, "home/single.html", context)

def terms(request):

    return render(request, "home/terms.html")
