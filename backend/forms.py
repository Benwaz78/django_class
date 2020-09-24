from django import forms
from frontend.models import Category, Post
from django.core import validators
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name", 
               widget=forms.TextInput(
               attrs={'class':'form-control', 'placeholder':'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
              widget=forms.Textarea(
             attrs={'class':'form-control'}
              ))
    catch_bot = forms.CharField(required=False, 
                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field
    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name')
        if Category.objects.filter(cat_name=cat).exists():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    class Meta():
        fields = '__all__'
        model = Category


class PostForm(forms.ModelForm):
    pst_title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'})
    )
    pst_content = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'})
    )
    pst_img = forms.ImageField()
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label='Please Choose', 
        widget=forms.Select(attrs={'class': 'form-control'}))
    featured = forms.BooleanField(required=False)

    class Meta():
        exclude = ['created', ]
        model = Post

