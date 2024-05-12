from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone

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
        fields = ('email', 'username', 'password1', 'password2', 'orgbox','year_section', 'sem_1','sem_2')

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
    
    def save(self, commit=True):
            user = super().save(commit=False)
            sem_1_duration = timezone.now() 
            sem_2_duration = timezone.now() 
            user.sem_1 = sem_1_duration
            user.sem_2 = sem_2_duration
            if commit:
                user.save()
            return user
        
        
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
        
        
class OfficerYearForm(forms.ModelForm):
    YEAR_CHOICES = [
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        (2031, '2031'),
        (2032, '2032'),
        (2033, '2033'),
        (2034, '2034'),
        (2035, '2035'),
        (2036, '2036'),
        (2037, '2037'),
        (2038, '2038'),
        (2039, '2039'),
        (2040, '2040'),
        (2041, '2041'),
        (2042, '2042'),
        (2043, '2043'),
        (2044, '2044'),
        (2045, '2045'),
        (2046, '2046'),
        (2047, '2047'),
        (2048, '2048'),
        (2049, '2049'),
        (2050, '2050'),
    ]
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    class Meta:
        model = OfficerYear
        fields = ['year']
        
