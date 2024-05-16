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
    path('view-user/<int:user_id>/',views.view_user, name='view-user'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
    
    path('edit-banner/<int:id>/', views.edit_banner, name='edit-banner'),
    path('edit-about/<int:id>/', views.edit_about, name='edit-about'),

    
    path('admin-users/',views.admin_user, name='admin-user'),
    path('admin-highlights/',views.admin_highlights, name='admin-highlights'),
    path('admin-register/', views.admin_register, name='admin-register'),
    
    path('admin-create-payment/',views.create_payment, name='admin-create-payment'),
    path('edit-payment/<int:id>/', views.edit_payment, name='edit-payment'),
    path('admin-vision-mission-goal/', views.vision_mission_goal, name='admin-vision-mission-goal'),
    path('edit-vmg/<int:id>/', views.edit_vmg, name='edit-vmg'),
    path('admin-about-us-context/', views.about_us_context, name='admin-about-us-context'),
    path('edit-context/<int:id>/', views.edit_context, name='edit-context'),
    
    path('home-officer/', views.homepage_officer, name='home-officer'),
    path('executive/', views.executive, name='executive'),
    path('documentation/', views.documentation, name='documentation'),
    path('esports/', views.esports, name='esports'),
    path('multimedia/', views.multimedia, name='multimedia'),
    path('programming/', views.programming, name='programming'),
    path('writers/', views.writers, name='writers'),
    path('social-media/', views.social_media, name='social-media'),
    path('executive-banner/', views.executive_banner, name='executive-banner'),
    path('marketing/', views.marketing, name='marketing'),
    path('adviser/', views.adviser, name='adviser'),
    path('board-member/', views.board_member, name='board-member'),
    
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    
    path('sub-1-add/<int:user_id>/',views.sem_1_add, name='sub-1-add'),
    path('sub-1-remove/<int:user_id>/',views.sem_1_remove, name='sub-1-remove'),
    path('sub-2-add/<int:user_id>/',views.sem_2_add, name='sub-2-add'),
    path('sub-2-remove/<int:user_id>/',views.sem_2_remove, name='sub-2-remove'),
    
    path('delete-highlight/<int:highlight_id>/', views.delete_highlight, name='delete_highlight'),
    
    path('events/', views.events, name='events'),
    
    path('about-us/', views.about_us, name='about-us'),
    
    path('membership/', views.membership, name='membership'),
    # path('add-sub/<int:user_id>/',views.add_sub, name='add-sub'),
    
    path('create-payment-intent/', views.create_payment_intent, name='create-payment-intent'),
    
    path('payment/', views.payment, name='payment'),
    path('gpayment/', views.gpayment, name='gpayment'),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)