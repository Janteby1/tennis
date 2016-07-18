from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from .models import Scores

class AddScoresForm(forms.ModelForm):
    player = forms.CharField() # get the input directly from the user
    court = forms.CharField() # get the input directly from the user
    won = forms.CharField() # get the input directly from the user
    loss = forms.CharField() # get the input directly from the user

    class Meta:
        model = Scores
        fields = [
            'player','court','won', 'loss',
        ]

