from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class newListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['finalBuyer','created_date', 'currentBid','active','watchers','user']
        widgets = {
            'category': forms.Select(attrs={
                'class':'form-control',
                'style': 'max-width: 300px;'}),
            'picture': forms.FileInput(attrs={
                'class':'form-control',
                'style': 'max-width: 300px;'}),
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }),
            'startingBid': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                })
        }

class newBidForm(ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        exclude = ['auction', 'user', 'date']
        widgets = {
        'offer': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                })
        }
