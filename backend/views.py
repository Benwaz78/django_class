from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from frontend.models import Post, Category

from backend.forms import CategoryForm, PostForm, ContactForm

from django.conf import settings

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:index')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')

@login_required(login_url='/dashboard/')
def confirm_logout(request):
    return render(request, 'backend/confirm.html')

@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')

@login_required(login_url='/dashboard/')
def index(request):
    return render(request, 'backend/index.html')

def register(request):
    return render(request, 'frontend/register.html')

@login_required(login_url='/dashboard/')
def categroy_form(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Category Created')
    else:
        cat_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat':cat_form})

@login_required(login_url='/dashboard/')
def post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post Created')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-post.html', {'post': post_form})


def contact_form(request):
    if request.method == 'POST':
        contform = ContactForm(request.POST)
        if contform.is_valid():
            contform.save()
            subject = contform.cleaned_data.get('subject')
            name = contform.cleaned_data.get('name')
            email = contform.cleaned_data.get('email')
            gender = contform.cleaned_data.get('gender')
            referer = contform.cleaned_data.get('referer')
            my_dict = {'name':name, 'email':email, 'gender':gender, 'referer':referer}
            html_message = render_to_string('frontend/mail-template.html', my_dict)
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            mail.send_mail(subject, plain_message, from_email, ['uwazie.benedict@alabiansolutions.com',], html_message=html_message)
            messages.success(request, 'Form is saved')
    else:
        contform = ContactForm()
    return render(request, 'frontend/contact.html', {'con': contform})


@login_required(login_url='/dashboard/')
def edit_post(request, post_id):
    single_post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=single_post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post Edited')
    else:
        post_form = PostForm(instance=single_post)
    return render(request, 'backend/edit-post.html', {'edit_post': post_form})
    




