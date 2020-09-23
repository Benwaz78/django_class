from django.shortcuts import render
from django.http import HttpResponse
from frontend.models import Post, Category, Service
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    home_post = Post.objects.filter(featured=True).order_by('-created')[:3]
    home_serv = Service.objects.all()[:3]
    args = {'home_post':home_post, 'home_serv':home_serv}
    return render(request, 'frontend/index.html', args)

def about(request):
    return render(request, 'frontend/about.html')


def all_post(request):
	all_post = Post.objects.all()
	return render(request, 'frontend/post-list.html', {'posts':all_post})

def post_from_cat(request, cat_id):
	post_cat = Post.objects.filter(category__id=cat_id)
	return render(request, 'frontend/posts-cat.html', {'post_cat':post_cat})


def single_post(request, post_id):
    try:
        single = Post.objects.get(id=post_id)
        return render(request, 'frontend/single-post.html', {'single_post': single})
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    




def contact(request):
    return render(request, 'frontend/contact.html')


def service(request):
    serv = Service.objects.all()
    return render(request, 'frontend/services.html', {'sv':serv})


def users(request):
    return render(request, 'frontend/users.html')


