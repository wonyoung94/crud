from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    # return redirect('/index/') #인덱스로 가는 경로
    return redirect(f'/posts/{post.id}/') #작성한 글로 가는경로

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')

def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'edit.html', context)

def update(request, id):
    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    #기존데이터
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
