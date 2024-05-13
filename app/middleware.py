from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import auth
from .models import User

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_active and not request.user.is_superuser:
            if request.path.startswith(reverse('admin:index')):
                return redirect('home') 
        return self.get_response(request)
    
    

class RegistrationExpirationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = timezone.now()
            user = User.objects.get(pk=request.user.pk)
            if user.sem_1 and user.sem_2:
                if current_time <= user.sem_1 or current_time <= user.sem_2:
                    pass
                else:
                    auth.logout(request)
            
        response = self.get_response(request)
        return response