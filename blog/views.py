from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from blog.models import post
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    posts = post.objects.all().order_by('-timestamp')[:4]

    context = {
    'posts' : posts,
    'next': 2,
    'previous':0

    }

    return render(request,'index.html',context)

def pages(request,page):
    posts = post.objects.all().order_by('-timestamp')[4*(int(page) - 1):4*int(page)]

    context = {
    'posts' : posts,
    'next' : int(page)+1,
    'previous': int(page)-1
    }

    return render(request,'index.html',context)


def detail(request,id):

    try:
        posts = post.objects.get(id=id)
    except ObjectDoesNotExist:
        posts = 'wut'
    context = {
    'posts' : posts,
    'previous':int(id)-1,
    'next': int(id)+1
    }
    return render(request,'detail.html',context)


def search(request):
    a,b,search_text = str(request.body).split('=')
    search_text = search_text[0:-1]
    print( search_text)

    posts = post.objects.filter(Q(title__contains=str(search_text)) | Q(author__contains=str(search_text) )).order_by('-timestamp')[:20]
    context = {
    'posts' : posts,
    
    }

    return render(request,'index.html',context)
