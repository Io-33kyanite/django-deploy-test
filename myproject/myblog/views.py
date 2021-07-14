from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

def index(request):
    # return HttpResponse("Hello Django!!")
    # return render(request, 'myblog/index.html')
    posts = Post.objects.order_by('-published')
    return render(request, 'myblog/index.html', {'posts': posts})

def showBody(request, id):
    object = get_object_or_404(Post, pk=id)
    post = {
        'post':object,
    }
    return render(request, 'myblog/body.html', post)