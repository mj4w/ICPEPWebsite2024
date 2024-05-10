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
# Create your views here.
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
                    login(request, user)
                   
                    if user.username == "admin":
                        messages.success(request,'Welcome sa DARK WEB!')
                        return redirect('admin-user')
                    else:
                        messages.success(request,'Successfully Login!')
                        return redirect('home')
                
            else:
                # Form is not valid
                messages.error(request, 'Login Error: Please enter valid credentials.')
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
                login(request, user)
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
    return redirect('home')


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
    users = User.objects.all()
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
    message = f'Your account has been approved. You can now <a href="{login_url}">login to your account</a>.'
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


@require_http_methods(["DELETE"])
def delete_highlight(request, highlight_id):
    highlights = get_object_or_404(HighlightsEvent, id=highlight_id)
    highlights.delete()
    return JsonResponse({'message': 'Highlight deleted successfully'}, status=204)

def events(request):
    return render(request,'events.html')

def about_us(request):
    return render(request,'about_us.html')