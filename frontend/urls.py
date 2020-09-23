from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
     path('', views.about, name='about'),
    path('service-page/', views.service, name='service'),
    path('post-list/', views.all_post, name='all_post'),
    path('post-cat/<int:cat_id>/', views.post_from_cat, name='post_from_cat'),
    path('single-post/<int:post_id>/', views.single_post, name='single_post'),
    path('contact/', views.contact, name='contact'),
    path('users/', views.users, name='users'),

]
