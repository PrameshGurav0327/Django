from django import forms
# from django.core import validators

# def start_with_a(val):
#     x = val[0]
#     if x.isdigit():
#         raise forms.ValidationError("Name don't starts with Number")
    
class MarvelForm(forms.Form):
    name = forms.CharField()
    heroic_name = forms.CharField()