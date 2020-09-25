from django import forms

def check_for_c(value):
    if value[0].capitalize() != 'C':
        raise forms.ValidationError('Name must start with "C"')
