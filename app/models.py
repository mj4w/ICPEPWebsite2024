from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager,AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True,null=True,max_length=100)
    email = models.EmailField(unique=True,null=True)
    orgbox = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile-images/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(blank=True, null=True)
    YEAR_SECTION_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]
    
    year_section = models.CharField(max_length=10, choices=YEAR_SECTION_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    USERNAME_FIELDS = 'username'
    REQUIRED_FIELDS = []

#homepage
    
class Banner(models.Model):
    sub_text = models.CharField(max_length=100,blank=True)
    primary_text = models.CharField(max_length=100,blank=True)
    primary_sub = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.primary_text
    
class AboutPic(models.Model):
    image = models.ImageField(upload_to='about-pic-upload/')
    image_title = models.CharField(max_length=50,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.image_title
    
class HighlightsEvent(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='highlights-event/')
    title = models.CharField(max_length=200, blank=True)
    time = models.TimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True, verbose_name="Start ng date")
    date_from = models.DateField(blank=True, null=True, verbose_name="End ng date")
    location = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True, null=True)
    link_desc = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=100, blank=True, verbose_name="Hosted By")
    learn_more = models.URLField(max_length=255,blank=True)
    
    def __str__(self):
        return self.title
    
class SoftwareTools(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='software-tools/')
    
class SoftwareToolsResource(models.Model):
    url = models.URLField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length = 255, blank=True, null=True)
    image = models.ImageField(upload_to='software-resources/')
    desc = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.title