from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime,timedelta,timezone
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import SuspiciousOperation
from .forms import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.core.files.storage import default_storage
import os


def home(request):
    current_date = datetime.now().date()
    
    banner = Banner.objects.first()
    aboutpic = AboutPic.objects.first()
    highlights = HighlightsEvent.objects.all().order_by('-date_from')
    softwaretools = SoftwareTools.objects.all()

    context = {
        'banner': banner,
        'aboutpic': aboutpic,
        'highlights': highlights,
        'softwaretools': softwaretools,
    }

    return render(request,'homepage.html',context)

def resources(request):
    resource_docu = SoftwareToolsResource.objects.all()
    return render(request,'resources_docu.html',{'resource_docu':resource_docu})

def highlights(request,pk):
    current_date = datetime.now().date()
    highlights = HighlightsEvent.objects.get(id=pk)

    if highlights.date_to is not None and highlights.date_from is not None:
        if highlights.date_to <= current_date <= highlights.date_from:
            ping = 1
        else:
            ping = 0
    else:
        ping = 0
    print(ping)
    context = {'highlights': highlights,'ping':ping}
    return render(request,'highlights.html',context)


# accounts
def login_user(request):
    try: 
        if request.method == 'POST':
            form_login = LoginForm(request.POST or None, data=request.POST)
            if form_login.is_valid():
                user = authenticate(request, username=form_login.cleaned_data['username'], password=form_login.cleaned_data['password'])
                if user is not None:
                    if user.sem_1 is not None and user.sem_2 is not None:
                        current_time = timezone.now()
                        if user.sem_1 <= current_time or user.sem_2 <= current_time:
                            messages.error(request, 'Your account has expired or not activate yet.')
                            return redirect('membership')
                    login(request, user)
                    
                    if user.is_superuser:
                        messages.success(request, 'Welcome to the admin panel!')
                        return redirect('admin-user')
                    elif user.is_staff:
                        messages.success(request, 'Welcome to the admin panel!')
                        return redirect('home-officer')
                    else:
                        next_url = request.GET.get('next', reverse('home')) 
                        messages.success(request, 'Successfully logged in!')
                        return redirect(next_url)
                
            else:
                messages.error(request, 'Login Error: Please enter valid credentials.')
        else:
            if 'next' in request.GET and 'admin' in request.GET['next'] and not request.user.is_superuser:
                messages.error(request, 'You are not authorized to access the admin login page.')
                return redirect(reverse('home'))
    except SuspiciousOperation as e:
        messages.error(request, f'CSRF Verification Failed: {str(e)}')
        return redirect('home')
    form_login = LoginForm()
    return render(request, 'accounts/login.html',{'form_login': form_login})

def register_user(request):
    try:
        if request.method == 'POST':
            form_register = RegisterForm(request.POST or None)
            if form_register.is_valid():
                user = form_register.save(commit=False)
                user.is_active = False  # Set user registration as pending
                user.save()
                # login(request, user)
                student_num = user.username
                subject = 'Pending Registration: {}'.format(student_num)
                message = render_to_string('email_template/email_template_register.html', {
                    'email': user.email,
                })
                recipient_list = [user.email]
                email = EmailMessage(subject, message, to=recipient_list)
                email.content_subtype = 'html' 
                email.send()
                messages.success(request, 'Registration Confirmation Sent in your GMAIL')
                return redirect('home')
            else:
                for field, errors in form_register.errors.items():
                    for error in errors:
                        messages.error(request, f"Registration Error: {field.capitalize()} - {error}")
    except SuspiciousOperation as e:
        messages.error(request, f'CSRF Verification Failed: {str(e)}')
        return redirect('home')
    form_register = RegisterForm()
    return render(request, 'accounts/register.html', {'form_register': form_register})


def logout_user(request):
    logout(request)
    messages.success(request,'Thankyou For Visiting!')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# coming soon
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')



# admin page
@login_required
def admin_dashboard(request):
    if request.method == 'POST':
        if 'subText' in request.POST and 'primaryText' in request.POST and 'primarySub' in request.POST:
            sub_text = request.POST['subText']
            primary_text = request.POST['primaryText']
            primary_sub = request.POST['primarySub']
            description = request.POST['description']
            Banner.objects.create(sub_text=sub_text, primary_text=primary_text, primary_sub=primary_sub, description=description)
            
        elif request.method == 'POST' and 'title' in request.POST and 'description' in request.POST and 'image' in request.FILES:
            image = request.FILES.get('image')  
            title = request.POST['title']
            description = request.POST['description']
            AboutPic.objects.create(image_title=title, description=description,image=image)
        
        return redirect('admin-dashboard')
    else:
        banners = Banner.objects.all()
        about_pics = AboutPic.objects.all()
        
        return render(request, 'admin/dashboard.html', {'banners': banners, 'about_pics': about_pics})

@login_required
def edit_banner(request, id):
    banner = get_object_or_404(Banner, pk=id)
    if request.method == 'POST':
        sub_text = request.POST.get('subText')
        primary_text = request.POST.get('primaryText')
        primary_sub = request.POST.get('primarySub')
        description = request.POST.get('description')
        
        banner.sub_text = sub_text
        banner.primary_text = primary_text
        banner.primary_sub = primary_sub
        banner.description = description
        banner.save()
        
        return JsonResponse({'message': 'Banner Updated Successfully'})
    else:
        banner_data = {
            'sub_text': banner.sub_text,
            'primary_text': banner.primary_text,
            'primary_sub': banner.primary_sub,
            'description': banner.description,
        }
        return JsonResponse(banner_data)
@login_required
def edit_about(request, id):
    about = get_object_or_404(AboutPic, pk=id)
    
    if request.method == "POST":
        image_file = request.FILES.get('image')
        if image_file:
            file_path = default_storage.save(image_file.name, image_file)
            if about.image:
                default_storage.delete(about.image.name)

            about.image = file_path
        
        about.image_title = request.POST.get('imageTitle', about.image_title)
        about.description = request.POST.get('description', about.description)
        
        about.save() 
        
        return JsonResponse({'message': 'About Updated Successfully'})
    else:
        about_data = {
            'image': about.image.url if about.image else '',  
            'imageTitle': about.image_title,
            'description': about.description,
        }
        return JsonResponse(about_data)
    
@login_required
def admin_user(request):
    users = User.objects.filter(is_superuser=False, is_staff=False)
    if request.method == 'POST':

        # Get form data
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        org_box = request.POST.get('orgBox') == 'on' 
        is_staff = request.POST.get('isStaff') == 'on'  
        is_active = request.POST.get('isActive') == 'on'
        user_image = request.FILES.get('userImage', None) 
        
        # Create user
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User email already exists.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'User username already exists.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = is_staff
            user.is_active = is_active
            user.image = user_image
            user.org_box = org_box
            user.save()

            messages.success(request, 'User created successfully.')
            return redirect('admin-user')

    else:
        return render(request, 'admin/view_user.html',{'users':users})
    return render(request, 'admin/view_user.html',{'users':users})

@require_POST
def approve_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = True
    user.save()

    subject = 'Account Approval Notification'
    login_url = settings.LOGIN_URL
    message = f'Your account has been activated. Please ensure that you have registered with our ICPEP organization. Once registered, you can proceed to log in. Please follow the link to access your account: <a href="{login_url}">Login to your account</a>.'
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list, html_message=message)

    return JsonResponse({'message': 'User approved successfully'})

@require_POST
def reject_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    
    subject = 'Account Rejected'
    message = f'Your account has been disapproved. Thanks for signing-up.'
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list, html_message=message)
    return JsonResponse({'message': 'User rejected successfully'})

@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'}, status=204)

@login_required
def admin_highlights(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        image = request.FILES.get('image')
        title = request.POST.get('title')
        time = request.POST.get('time')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        location = request.POST.get('location')
        description = request.POST.get('description')
        linkDescription = request.POST.get('linkDescription')
        hostedBy = request.POST.get('hostedBy')
        learnMore = request.POST.get('learnMore')
        
        new_event = HighlightsEvent(
            url=url,
            image=image,
            title=title,
            time=time,
            date_to=startDate,
            date_from=endDate,
            location=location,
            desc=description,
            link_desc=linkDescription,
            details=hostedBy,
            learn_more=learnMore
        )      

        new_event.save()
        messages.success(request,'Add Events Successfully!')
        
        return redirect('admin-highlights')

    highlights = HighlightsEvent.objects.all()
    return render(request, 'admin/view_highlights.html', {'highlights': highlights})

@require_http_methods(["POST"])
def send_highlight_email(request, event_id):
    if request.method == 'POST':
        try:
            event = HighlightsEvent.objects.get(pk=event_id)

            # Get other relevant event details
            highlights_url = f"{settings.HIGHLIGHTS}{event_id}/"
            event_title = event.title
            event_url = event.url
            event_hosted = event.details
            event_description = event.desc

            users = User.objects.filter(is_active=True)

            for user in users:
                subject = 'New Event: {}'.format(event_title)
                message = render_to_string('email_template/event_template.html', {
                    'name': user.last_name,
                    'event_title': event_title,
                    'event_url': event_url,
                    'event_id': highlights_url,
                    'event_hosted': event_hosted,
                    'event_description': event_description,
                })
                recipient_list = [user.email]
                email = EmailMessage(subject, message, to=recipient_list)
                email.content_subtype = 'html'
                email.send()

            return JsonResponse({'success': True, 'message': 'Emails sent successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
@login_required    
def view_highlight(request, highlight_id):
    from django.core.serializers.json import DjangoJSONEncoder
    highlight = get_object_or_404(HighlightsEvent, id=highlight_id)
    image_url = highlight.image.url if highlight.image else None
    highlight_data = {
        'title': highlight.title,
        'description': highlight.desc,
        'url': highlight.url,
        'image': image_url,
        'time': highlight.time,
        'date_from': highlight.date_from,
        'date_to': highlight.date_to,
        'location': highlight.location,
        'details': highlight.details,
        'learn_more': highlight.learn_more,
        'link_desc': highlight.link_desc,
    }
    return JsonResponse(highlight_data, encoder=DjangoJSONEncoder)

@login_required    
def view_user(request, user_id):
    from django.core.serializers.json import DjangoJSONEncoder
    user = get_object_or_404(User, id=user_id)
    image_url = user.image.url if user.image else None
    user_data = {
        'username': user.username,
        'email': user.email,
        'orgbox': user.orgbox,
        'is_active': user.is_active,
        'image': image_url,
        'date_joined': user.date_joined,
        'sem_1': user.sem_1,
        'sem_2': user.sem_2,
    }
    return JsonResponse(user_data, encoder=DjangoJSONEncoder)

@login_required
def homepage_officer(request):
    return render(request,'officer/homepage.html')


@login_required
def executive(request):
    year = OfficerYearForm()
    executives = ExecutiveOfficer.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save()
            ExecutiveOfficer.objects.create(
                year = year_instance,
                president = request.POST.get('president_name'),
                president_img = request.FILES.get('president_image'),
                vp_internal = request.POST.get('vp_internal_name'),
                vp_internal_img = request.FILES.get('vp_internal_image'),
                vp_external = request.POST.get('vp_external_name'),
                vp_external_img = request.FILES.get('vp_external_image'),
                secretary = request.POST.get('secretary'),
                secretary_img = request.FILES.get('secretary_image'),
                assistant_secretary = request.POST.get('asst_secretary_name'),
                assistant_secretary_img = request.FILES.get('asst_secretary_image'),
                treasurer = request.POST.get('treasurer_name'),
                treasurer_img = request.FILES.get('treasurer_image'),
                assistant_treasurer = request.POST.get('asst_treasurer_name'),
                assistant_treasurer_img = request.FILES.get('asst_treasurer_image'),
                auditor = request.POST.get('auditor_name'),
                auditor_img = request.FILES.get('auditor_image'),
                pro = request.POST.get('pro_name'),
                pro_img = request.FILES.get('pro_image'),
            )
            messages.success(request, 'Executive Officers data saved successfully.')
            return redirect('executive') 

    messages.success(request,'Welcome to Executive Officer')
    return render(request,'officer/executive.html', {'year': year,'executives': executives})

@login_required
def documentation(request):
    return render(request,'officer/documentation.html')

@login_required
def esports(request):
    return render(request,'officer/esports.html')

@login_required
def multimedia(request):
    return render(request,'officer/multimedia.html')

@login_required
def programming(request):
    return render(request,'officer/programming.html')

@login_required
def writers(request):
    return render(request,'officer/writers.html')

@require_http_methods(["DELETE"])
def delete_highlight(request, highlight_id):
    highlights = get_object_or_404(HighlightsEvent, id=highlight_id)
    highlights.delete()
    return JsonResponse({'message': 'Highlight deleted successfully'}, status=204)

@login_required
def admin_register(request):
    users = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request,'admin/register.html', {'users': users})

def admin_logout(request):
    logout(request)
    messages.success(request,'Thanks Admin!')
    return redirect('home')


def events(request):
    highlights = HighlightsEvent.objects.filter(date_from__gte=timezone.now()).order_by('date_from')
    return render(request, 'events.html', {'highlights': highlights})

def about_us(request):
    return render(request,'about_us.html')

def membership(request):
    september = ""
    january = ""
    subscription_status = ""
    date_now = timezone.now()
    sub = 0
    
    if request.user.is_authenticated:
        user_register = request.user.sem_1
        if user_register and user_register > timezone.now():
            # subscription_status = "Your registration is active."
            sub = 1
        else:
            # subscription_status = "Your registration has expired. Renew now!"
            sub = 2

    current_month = datetime.now().month
    if current_month in [1, 2, 3, 4, 5, 6, 7, 8]:
        january = "This is the second semester. Register now!"
    elif current_month in [9, 10, 11, 12]:
        september = "This is the first semester. Register now!"

    return render(request, 'membership.html', {'september': september, 'january': january, 'subscription_status': subscription_status, 'date_now': date_now,'sub':sub})

def sem_1_add(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.sem_1 is None:
        user.sem_1 = timezone.now() + timedelta(days=4*30) 
    else:
        user.sem_1 += timedelta(days=4*30)  
    user.save()
    return JsonResponse({'message': 'Sem 1 activated'})

def sem_1_remove(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if user.sem_1 is not None:
        new_sem_date = user.sem_1 - timedelta(days=30 * 4)
        user.sem_1 = new_sem_date
        user.save()
        
    return JsonResponse({'message': 'Sem 1 date decreased by 4 months'})

def sem_2_add(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.sem_2 is None:
        user.sem_2 = timezone.now() + timedelta(days=8*30) 
    else:
        user.sem_2 += timedelta(days=8*30)
    user.save()
    return JsonResponse({'message': 'Sem 2 activated'})

def sem_2_remove(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if user.sem_2 is not None:
        new_sem_date = user.sem_2 - timedelta(days=30 * 8)
        user.sem_2 = new_sem_date
        user.save()
        
    return JsonResponse({'message': 'Sem 1 date decreased by 4 months'})
# def add_sub(request, user_id):
#     add = get_object_or_404(User, id=user_id)
#     current_expiration = add.date_expired
#     if not current_expiration or current_expiration < timezone.now():
#         current_expiration = timezone.now()
#     new_expiration = current_expiration + timedelta(days=365)
#     add.date_expired = new_expiration
#     add.save()
#     return JsonResponse({'message': '+1 Year subscription'})

import requests
def create_payment_intent(request):
    url = "https://api.paymongo.com/v1/payment_intents"
    payload = {
        "data": {
            "attributes": {
                "amount": 5000,
                "payment_method_allowed": ["gcash"],
                "payment_method_options": {"card": {"request_three_d_secure": "any"}},
                "currency": "PHP",
                "capture_type": "automatic"
            }
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic c2tfdGVzdF9yYjRrWW1BTnBWVVJRclZHa1dXZk1uTk06"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    return JsonResponse(data)

def payment(request):
    return render(request, 'payment.html')

def gpayment(request):
    payment = Payment.objects.all()
    return render(request, 'gcash_payment/gpayment.html',{'payment':payment})

