from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.


def hoem_page(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home_page.html', context)


def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    return render(request, 'post_details.html', context)
