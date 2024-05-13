from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def restrict_non_superuser(view_func):
    @user_passes_test(lambda user: user.is_authenticated and user.is_active and user.is_superuser)
    def _wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def restrict_non_staff(view_func):
    @user_passes_test(lambda user: user.is_authenticated and user.is_active and user.is_staff)
    def _wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return _wrapped_view
