from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('home/', views.index, name='index'),
    path('login-page/', views.login, name='login'),
    path('category-page/', views.categroy_form, name='categroy_form'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('register-page/', views.register, name='register'),
]
