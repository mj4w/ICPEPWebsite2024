from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home, name='home'),
    path('resources/',views.resources, name='resources'),
    path('highlights/<int:pk>/',views.highlights, name='highlights'),
    path('login/', views.login_user, name='login-user'),
    path('sign-up/',views.register_user, name='register-user'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    path('log-out/',views.logout_user, name='log-out'),
    
    path('admin-dashboard/',views.admin_dashboard, name='admin-dashboard'),
    path('send-email/<int:event_id>/',views.send_highlight_email, name='send-email'),
    path('view-highlight/<int:highlight_id>/',views.view_highlight, name='view-highlight'),
    
    path('edit-banner/<int:id>/', views.edit_banner, name='edit-banner'),
    path('edit-about/<int:id>/', views.edit_about, name='edit-about'),

    
    path('admin-users/',views.admin_user, name='admin-user'),
    path('admin-highlights/',views.admin_highlights, name='admin-highlights'),
    
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    
    path('delete-highlight/<int:highlight_id>/', views.delete_highlight, name='delete_highlight'),
    
    path('events/', views.events, name='events'),
    
    path('about-us', views.about_us, name='about-us'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)