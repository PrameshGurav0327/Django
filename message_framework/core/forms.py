from django import forms
from . models import MarvelModel


class MarvelForm(forms.ModelForm):
    class Meta:
        model = MarvelModel
        fields=['name','heroic_name']

        #applying CSS classes to form fields using widgets
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'heroic_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heroic name'})
        }

        label = {
            "name" : "Avenger Name",
            "heroic_name" : "Heroic Name"
        }

        help_text = {
            "name" : "Enter the name of the Avenger",
            "heroic_name" : "Enter the Avenger's name"
        }
