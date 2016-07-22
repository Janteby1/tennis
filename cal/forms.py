from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from .models import Scores, Games

class AddScoresForm(forms.ModelForm):
    player = forms.CharField() # get the input directly from the user
    court = forms.IntegerField() # get the input directly from the user
    playerwon = forms.IntegerField() # get the input directly from the user
    playerloss = forms.IntegerField() # get the input directly from the user
    set = forms.IntegerField() # get the input directly from the user
    round = forms.IntegerField() # get the input directly from the user

    class Meta:
        model = Scores
        fields = [
            'court','set','player', 'playerwon', 'playerloss', 'round',
        ]

class AddGamesForm(forms.ModelForm):
    player = forms.CharField() # get the input directly from the user
    court = forms.IntegerField() # get the input directly from the user
    playerwon = forms.IntegerField() # get the input directly from the user
    playerloss = forms.IntegerField() # get the input directly from the user
    set = forms.IntegerField() # get the input directly from the user
    round = forms.IntegerField() # get the input directly from the user

    class Meta:
        model = Games
        fields = [
            'court','set','player', 'playerwon', 'playerloss', 'round',
        ]
