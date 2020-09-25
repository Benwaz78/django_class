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


class ContactForm(forms.ModelForm):
	name = forms.CharField(validators=[check_for_c], widget=forms.TextInput(
	    attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
	subject = forms.CharField(widget=forms.TextInput(
	    attrs={'class': 'form-control', 'placeholder': 'Enter Subject', 'max_length': 10}))
	email = forms.EmailField(widget=forms.EmailInput(
	    attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
	verify_email = forms.EmailField(label='Email Again', widget=forms.EmailInput(
	    attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=GENDER_FIELD)
	referer = forms.ChoiceField(required=False, widget=forms.Select(
	    attrs={'class': 'form-control'}), choices=REFERER_FIELD)
	message = forms.CharField(required=False, widget=forms.Textarea(
	    attrs={'class': 'form-control'}))
	botcatcher = forms.CharField(widget=forms.HiddenInput(
	), required=False, validators=[validators.MaxLengthValidator(0)])

	# To validate just one field

	def clean_subject(self):
		subt = self.cleaned_data.get('subject')
		if 'Hello' not in subt:
			raise forms.ValidationError('You must include "Hello" in your subject')
		return subt

	# TO validate two fields (Fields that depend on each other)
	def clean(self):
		cleaned_data = super().clean()
		email1 = cleaned_data.get('email')
		email2 = cleaned_data.get('verify_email')
		if email1 != email2:
			self.add_error('email', 'The two emails must match')
		elif not email1.endswith('@alabiansolutions.com'):
			self.add_error('email', 'Your email must end with "@alabiansolutions"')

	class Meta():
		model = ContactModel
		fields = ('name', 'subject', 'email', 'verify_email',
		          'gender', 'referer', 'message')
