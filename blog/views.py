from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Q
from blog.models import post
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.
def home(request):
    posts = post.objects.all().order_by('-timestamp')[:5]

    context = {
    'posts' : posts,
    'next': 2,
    'previous':0

    }

    return render(request,'index.html',context)

def pages(request,page):
    posts = post.objects.all().order_by('-timestamp')[5*(int(page) - 1):5*int(page)]

    context = {
    'posts' : posts,
    'next' : int(page)+1,
    'previous': int(page)-1
    }

    return render(request,'index.html',context)


def detail(request,id,page_direction= 'null'):

    try:
        posts = post.objects.get(id=id)
        if page_direction == 'previous':
            return redirect(posts.get_previous_by_timestamp())
        elif page_direction == 'next' :
            return redirect(posts.get_next_by_timestamp())


    except ObjectDoesNotExist:
            posts = 'wut'
    context = {
    'posts' : posts,
    'previous':int(id)-1,
    'next': int(id)+1
    }
    return render(request,'detail.html',context)


def search(request,keyword='null'):

    if request.method == 'POST':
        return redirect('/search/'+str(request.POST['keyword']))

    search_text = keyword
    search_text = search_text
    # print( request.POST['keyword'])
    posts = post.objects.filter(Q(title__contains=str(search_text)) | Q(author__contains=str(search_text)) | Q(bodytext__contains = str(search_text)) ).order_by('-timestamp')[:]
    context = {
    'posts' : posts,
    'search' : True
    }

    return render(request,'index.html',context)
