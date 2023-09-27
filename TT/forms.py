from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import UserProfileModel, Room

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Custom validation logic
        
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain spaces.")
        return username

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class': 'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={ 'class':'form-control'}))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['firstName', 'lastName', 'dateOfBirth', 'picture']

        widgets = { 
            'firstName': forms.TextInput(attrs={'class':'form-control'}),
            'lastName': forms.TextInput(attrs={'class':'form-control'}),
            'dateOfBirth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'name': 'picture'})
        }

        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'dateOfBirth': 'DOB',
            'picture': 'Profile Picture'
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']