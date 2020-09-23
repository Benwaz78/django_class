from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    profile_pic = models.FileField(blank=True, null=True, upload_to='upload/')


class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Category Description')

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Category'


class Post(models.Model):
    pst_title = models.CharField(max_length=100)
    pst_content = models.TextField()
    pst_img = models.FileField(blank=True, null = True, upload_to='upload/')
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural='Post'


class Service(models.Model):
    srv_title = models.CharField(max_length=100)
    srv_content = models.TextField()

    def __str__(self):
        return self.srv_title

