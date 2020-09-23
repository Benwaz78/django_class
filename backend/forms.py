from django import forms
from frontend.models import Category
from django.core import validators


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