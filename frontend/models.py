from django.db import models
from django.contrib.auth.models import User
from backend.options import REFERER_FIELD, GENDER_FIELD, CHOOSE

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
    featured = models.BooleanField(default=False, blank=True)
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


class ContactModel(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	email = models.EmailField()
	gender = models.CharField(max_length=15, choices=GENDER_FIELD)
	referer = models.CharField(
	    max_length=30, choices=REFERER_FIELD, default=CHOOSE, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

