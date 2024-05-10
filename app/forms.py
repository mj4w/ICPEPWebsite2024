from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'input'})
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class':'input'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'input'})
    )
    # year_section = forms.CharField(
    #     label='Year & Section',
    #     widget=forms.TextInput(attrs={'class':'input'})
    # )

    class Meta: 
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'orgbox','year_section')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
            if not email.endswith('@bulsu.edu.ph'):
                raise forms.ValidationError('Only email addresses with @bulsu.edu.ph domain are allowed.')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered.")
        return email
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class':'input'})
    )

class AboutPicForm(forms.ModelForm):
    class Meta:
        model = AboutPic
        fields = ['image', 'image_title', 'description']

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['sub_text', 'primary_text', 'primary_sub', 'description']