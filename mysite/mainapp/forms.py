from django.forms import TextInput, Select
from django import forms
from .models import gift, Recipient


class Recipient(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Recipient\'s name',
            })
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = gift
        fields = ['recipient', 'gift_name', 'price', 'type', 'year']
        widgets = {
            'recipient': Select(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Recipient'
            }),
            'gift_name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Gift name'
            }),
            'price': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Price'
            }),
            'type': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Short Description'
            }),
            'year': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 30rem;',
                'placeholder': 'Year'
            }),
        }
