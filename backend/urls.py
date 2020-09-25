from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('home/', views.index, name='index'),
    path('login-page/', views.login, name='login'),
    path('category-page/', views.categroy_form, name='categroy_form'),
    path('post-form/', views.post_form, name='post_form'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('register-page/', views.register, name='register'),
    path('contact-page/', views.contact_form, name='contact_form')
]
