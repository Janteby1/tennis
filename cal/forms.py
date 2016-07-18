from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from .models import UserProfile, Events, Organization, Tags, TaggedTag


# form used to register a user
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "email",
            "phone", 
            "website",
            "industry"
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }


class AddEventForm(forms.ModelForm):
    date = forms.CharField() # get the input directly from the user
    place = forms.CharField() # get the input directly from the user
    address = forms.CharField() # get the input directly from the user

    price = forms.CharField() # get the input directly from the user
    description = forms.CharField() # get the input directly from the user
    phone = forms.CharField() # get the input directly from the user
    website = forms.CharField() # get the input directly from the user

    class Meta:
        model = Events
        fields = [
            'date','place','address',
            'price','description','phone','website'
        ]


# class AddTagsForm(forms.ModelForm):
#     tags = forms.CharField() # get the input directly from the user

#     class Meta:
#         model = TaggedTag
#         fields = ['tag', 'content_type', 'object_id', 'tagged_item']


# class OrgLoginForm(forms.ModelForm):
#     class Meta:
#         model = Organization
#         fields = [
#             "username",
#             "password",
#         ]
#         widgets = {
#             # this sets the input text area
#             "password": PasswordInput(),
#         }


# class AddEventForm(forms.Form):
#     date = forms.CharField() # get the input directly from the user
#     place = forms.CharField() # get the input directly from the user
#     address = forms.CharField() # get the input directly from the user

#     price = forms.CharField() # get the input directly from the user
#     description = forms.CharField() # get the input directly from the user
#     phone = forms.CharField() # get the input directly from the user
#     website = forms.CharField() # get the input directly from the user

#     def save(self, commit=True):
#         event = Events(**self.cleaned_data)
#         if commit == True:
#             super().save()
#         print (event)
#         return event


'''    
    organization = models.ForeignKey(Organization) # FK to the Organization table
    Tags
'''






        