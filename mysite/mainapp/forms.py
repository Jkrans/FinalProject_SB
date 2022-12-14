from urllib import request
from django.forms import TextInput, Select
from django import forms
from .models import gift, Recipient


class RecipientForm(forms.ModelForm):
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

    # I used ChatGPT to help solve the issue of filtering the select options based on the user that is logged in
    # This code was generated by ChatGPT, super cool.
    def __init__(self, *args, **kwargs):
        # Get the request object from the keyword arguments
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Filter the queryset for the recipient field by user
        if request:
            self.fields['recipient'].queryset = Recipient.objects.filter(
                user=request.user)
