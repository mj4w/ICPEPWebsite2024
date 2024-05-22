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
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.core.files.storage import default_storage
import os
from .decorators import restrict_non_superuser,restrict_non_staff
import pyrebase
from django.conf import settings
from .tasks import send_highlight_email_task

# import { initializeApp } from "firebase/app";
# import { getAnalytics } from "firebase/analytics";
# firebaseConfig = settings.FIREBASE_CONFIG

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# database = firebase.database()





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
                    current_time = timezone.now()
                    print(current_time)
                    print(current_time <= user.sem_1)
                    print(user.sem_2)
                    if user.sem_1 and user.sem_2:
                        if current_time <= user.sem_1 or current_time <= user.sem_2:
                            login(request, user)
                        else:
                            messages.error(request, 'Your account has expired or not activated yet.')
                            return redirect('membership')

                    login(request, user)
                    if user.is_superuser:
                        messages.success(request, 'Welcome to the admin panel!')
                        return redirect('admin-user')
                    elif user.is_staff:
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
                payment = Payment.objects.first()
                if payment:
                    image_url = request.build_absolute_uri(payment.image.url)
                else:
                    image_url = ''
                student_num = user.username
                subject = 'Pending Registration: {}'.format(student_num)
                message = render_to_string('email_template/email_template_register.html', {
                    'email': user.email,
                    'payment_email': payment.email,
                    'image_url': image_url,
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
@restrict_non_superuser
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
@restrict_non_superuser
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
@restrict_non_superuser
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
@restrict_non_superuser
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
    login_url = request.build_absolute_uri(reverse('login-user'))
    message = f'Your account has been verified. Please ensure that you have registered with our ICPEP organization. Once registered, you can proceed to log in. Please follow the link to access your account: <a href="{login_url}">Login to your account</a>.'
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
@restrict_non_superuser
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
        # Call Celery task asynchronously
        send_highlight_email_task.delay(event_id)
        return JsonResponse({'success': True, 'message': 'Emails sending task queued successfully'})
    
    
@login_required  
@restrict_non_superuser  
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
@restrict_non_superuser   
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
@restrict_non_superuser 
def create_payment(request):
    if request.method == "POST":
        acct_name = request.POST.get('acct_name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        Payment.objects.create(acct_name=acct_name, email=email, image=image)
    payments = Payment.objects.all()
    return render(request, 'admin/create_payment.html', {'payments': payments})

@login_required
@restrict_non_superuser
def edit_payment(request, id):
    payment = get_object_or_404(Payment, pk=id)
    
    if request.method == "POST":
        image_file = request.FILES.get('image')
        if image_file:
            file_path = default_storage.save(image_file.name, image_file)
            if payment.image:
                default_storage.delete(payment.image.name)

            payment.image = file_path
        
        payment.acct_name = request.POST.get('acct_name', payment.acct_name)
        payment.email = request.POST.get('email', payment.email)
        
        payment.save() 
        
        return JsonResponse({'message': 'payment Updated Successfully'})
    else:
        payment_data = {
            'image': payment.image.url if payment.image else '',  
            'acct_name': payment.acct_name,
            'email': payment.email,
        }
        return JsonResponse(payment_data)

@login_required 
@restrict_non_superuser 
def vision_mission_goal(request):
    if request.method == "POST":
        vision = request.POST.get('vision')
        mission = request.POST.get('mission')
        goal = request.POST.get('goal')
        VisionMissionGoal.objects.create(vision=vision, mission=mission, goal=goal)
    vmgs = VisionMissionGoal.objects.all()
    return render(request, 'admin/vision_mission_goal.html',{'vmgs':vmgs})

@login_required
@restrict_non_superuser
def edit_vmg(request, id):
    vision_mission_goal = get_object_or_404(VisionMissionGoal, pk=id)
    
    if request.method == "POST":
        
        vision_mission_goal.vision = request.POST.get('vision', vision_mission_goal.vision)
        vision_mission_goal.mission = request.POST.get('mission', vision_mission_goal.mission)
        vision_mission_goal.goal = request.POST.get('goal', vision_mission_goal.goal)
        
        vision_mission_goal.save() 
        
        return JsonResponse({'message': 'About Us Context Updated Successfully'})
    else:
        vision_mission_goal_data = {
            'vision': vision_mission_goal.vision,
            'mission': vision_mission_goal.mission,
            'goal': vision_mission_goal.goal,
        }
        return JsonResponse(vision_mission_goal_data)


@login_required 
@restrict_non_superuser 
def about_us_context(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        AboutUsContext.objects.create(title=title, description=description, image=image)
    about_us_contexts = AboutUsContext.objects.all()
    print(about_us_context)
    return render(request, 'admin/about_us_context.html', {'about_us_contexts': about_us_contexts})

@login_required
@restrict_non_superuser
def edit_context(request, id):
    about_us = get_object_or_404(AboutUsContext, pk=id)
    
    if request.method == "POST":
        image_file = request.FILES.get('image')
        if image_file:
            file_path = default_storage.save(image_file.name, image_file)
            if about_us.image:
                default_storage.delete(about_us.image.name)

            about_us.image = file_path
        
        about_us.title = request.POST.get('title', about_us.title)
        about_us.description = request.POST.get('description', about_us.description)
        
        about_us.save() 
        
        return JsonResponse({'message': 'About Us Context Updated Successfully'})
    else:
        about_us_data = {
            'image': about_us.image.url if about_us.image else '',  
            'title': about_us.title,
            'description': about_us.description,
        }
        return JsonResponse(about_us_data)


@login_required
@restrict_non_staff
def homepage_officer(request):
    return render(request,'officer/homepage.html')


@login_required
@restrict_non_staff
def executive_banner(request):
    year = OfficerYearForm()
    banners = ExecutiveBanner.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save()
            ExecutiveBanner.objects.create(
                year = year_instance,
                image = request.FILES.get('banner_image'),
            )
            messages.success(request, 'Executive Banner data saved successfully.')
            return redirect('executive-banner') 

    return render(request,'officer/banners.html', {'year': year,'banners':banners})
@login_required
@restrict_non_staff
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
                secretary = request.POST.get('secretary_name'),
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

    return render(request,'officer/executive.html', {'year': year,'executives':executives})

@login_required
@restrict_non_staff
def documentation(request):
    year = OfficerYearForm()
    documentations = DocumentationTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            documentation_head = request.POST.get('documentation_head')
            documentation_head_img = request.FILES.get('documentation_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'documentation_asst_{i}_name')
                assistant_img = request.FILES.get(f'documentation_asst_{i}_image')
                if assistant_name:
                    assistant, _ = DocumentationAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            documentation_instance = DocumentationTeam.objects.create(
                year=year_instance,
                documentation_head=documentation_head,
                documentation_head_img=documentation_head_img
            )
            documentation_instance.assistants.set(assistants)
            messages.success(request, 'Documentation Team data saved successfully.')
            return redirect('documentation') 
    return render(request,'officer/documentation.html', {'documentations':documentations,'year':year})

@login_required
@restrict_non_staff
def esports(request):
    year = OfficerYearForm()
    esports = EsportsTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            esports_head = request.POST.get('esports_head')
            esports_head_img = request.FILES.get('esports_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'esports_asst_{i}_name')
                assistant_img = request.FILES.get(f'esports_asst_{i}_image')
                if assistant_name:
                    assistant, _ = EsportsAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            esports_instance = EsportsTeam.objects.create(
                year=year_instance,
                esports_head=esports_head,
                esports_head_img=esports_head_img
            )
            esports_instance.assistants.set(assistants)
            messages.success(request, 'Esports Team data saved successfully.')
            return redirect('esports') 
    return render(request,'officer/esports.html',{'esportss':esports,'year':year})

@login_required
@restrict_non_staff
def multimedia(request):
    year = OfficerYearForm()
    multimedias = MultimediaTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            multimedia_head = request.POST.get('multimedia_head')
            multimedia_head_img = request.FILES.get('multimedia_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'multimedia_asst_{i}_name')
                assistant_img = request.FILES.get(f'multimedia_asst_{i}_image')
                if assistant_name:
                    assistant, _ = MultimediaAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            multimedia_instance = MultimediaTeam.objects.create(
                year=year_instance,
                multimedia_head=multimedia_head,
                multimedia_head_img=multimedia_head_img
            )
            multimedia_instance.assistants.set(assistants)
            messages.success(request, 'Multimedia Team data saved successfully.')
            return redirect('multimedia') 
    return render(request,'officer/multimedia.html',{'multimedias':multimedias,'year':year})

@login_required
@restrict_non_staff
def programming(request):
    year = OfficerYearForm()
    programmings = ProgrammingTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            programming_head = request.POST.get('programming_head')
            programming_head_img = request.FILES.get('programming_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'programming_asst_{i}_name')
                assistant_img = request.FILES.get(f'programming_asst_{i}_image')
                if assistant_name:
                    assistant, _ = ProgrammingAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            programming_instance = ProgrammingTeam.objects.create(
                year=year_instance,
                programming_head=programming_head,
                programming_head_img=programming_head_img
            )
            programming_instance.assistants.set(assistants)
            messages.success(request, 'Programming Team data saved successfully.')
            return redirect('programming') 
    return render(request,'officer/programming.html',{'programmings': programmings, 'year':year})

@login_required
@restrict_non_staff
def writers(request):
    year = OfficerYearForm()
    writers = WritersTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            writers_head = request.POST.get('writers_head')
            writers_head_img = request.FILES.get('writers_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'writers_asst_{i}_name')
                assistant_img = request.FILES.get(f'writers_asst_{i}_image')
                if assistant_name:
                    assistant, _ = WritersAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            writers_instance = WritersTeam.objects.create(
                year=year_instance,
                writers_head=writers_head,
                writers_head_img=writers_head_img
            )
            writers_instance.assistants.set(assistants)
            messages.success(request, 'Writers Team data saved successfully.')
            return redirect('writers') 
    return render(request,'officer/writers.html',{'writers': writers, 'year':year})

@login_required
@restrict_non_staff
def social_media(request):
    year = OfficerYearForm()
    socials = SocialMediaTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            social_media_head = request.POST.get('social_media_head')
            social_media_head_img = request.FILES.get('social_media_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'social_assist_{i}_name')
                assistant_img = request.FILES.get(f'social_assist_{i}_image')
                if assistant_name:
                    assistant, _ = SocialMediaAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            social_media_instance = SocialMediaTeam.objects.create(
                year=year_instance,
                social_media_head=social_media_head,
                social_media_head_img=social_media_head_img
            )
            social_media_instance.assistants.set(assistants)
            messages.success(request, 'Social Media Team data saved successfully.')
            return redirect('social-media') 
    return render(request,'officer/social_media.html',{'socials': socials, 'year':year})

@login_required
@restrict_non_staff
def marketing(request):
    year = OfficerYearForm()
    marketings = MarketingTeam.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            marketing_head = request.POST.get('marketing_head')
            marketing_head_img = request.FILES.get('marketing_image')
            assistants = []
            for i in range(1, 11):  
                assistant_name = request.POST.get(f'marketing_asst_{i}_name')
                assistant_img = request.FILES.get(f'marketing_asst_{i}_image')
                if assistant_name:
                    assistant, _ = MarketingTeamAssistant.objects.get_or_create(name=assistant_name)
                    if assistant_img:
                        assistant.image = assistant_img
                        assistant.save()
                    assistants.append(assistant)
            marketing_instance = MarketingTeam.objects.create(
                year=year_instance,
                marketing_team_head=marketing_head,
                marketing_team_img=marketing_head_img
            )
            marketing_instance.assistants.set(assistants)
            messages.success(request, 'Marketing Team data saved successfully.')
            return redirect('marketing') 
    return render(request,'officer/marketing.html',{'marketings': marketings, 'year':year})

@login_required
@restrict_non_staff
def adviser(request):
    year = OfficerYearForm()
    advisers = Adviser.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            name = request.POST.get('name')
            image = request.FILES.get('image')
            Adviser.objects.create(
                year=year_instance,
                name=name,
                image=image
            )
            messages.success(request, 'Adviser data saved successfully.')
            return redirect('adviser') 
    return render(request,'officer/adviser.html',{'advisers': advisers, 'year':year})

@login_required
@restrict_non_staff
def board_member(request):
    year = OfficerYearForm()
    boards = BoardMember.objects.all()
    if request.method == "POST":
        year = OfficerYearForm(request.POST)
        if year.is_valid():
            year_instance = year.save(commit=False)
            year_instance.save()
            position = request.POST.get('position')
            name = request.POST.get('name')
            image = request.FILES.get('image')
            BoardMember.objects.create(
                year=year_instance,
                name=name,
                image=image,
                position=position,
            )
            messages.success(request, 'Board Member data saved successfully.')
            return redirect('board-member') 
    return render(request,'officer/board_members.html',{'boards': boards, 'year':year})

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

def get_all_years():
    """
    Utility function to get all unique years from different models.
    """
    years = set()

    executive_years = ExecutiveOfficer.objects.values_list('year__year', flat=True).distinct()
    years.update(executive_years)
    
    multimedia_years = MultimediaTeam.objects.values_list('year__year', flat=True).distinct()
    years.update(multimedia_years)

    programming_years = ProgrammingTeam.objects.values_list('year__year', flat=True).distinct()
    years.update(programming_years)
    
    
    return sorted(years)


def about_us(request):
    all_years = get_all_years()
    print(all_years)

    selected_year = request.GET.get('selected_year')

    current_year = datetime.now().year
    print(selected_year)
    if not selected_year:
        selected_year = f"{current_year}-{current_year + 1}"

    try:
        latest_year = OfficerYear.objects.latest('year')
    except ObjectDoesNotExist:
        latest_year = None  

    latest_executives = ExecutiveOfficer.objects.filter(year__year=selected_year).first()

    latest_programming = ProgrammingTeam.objects.filter(year__year=selected_year).first()
    assistants_prog = latest_programming.assistants.all() if latest_programming else []

    latest_documentation = DocumentationTeam.objects.filter(year__year=selected_year).first()
    assistants_docu = latest_documentation.assistants.all() if latest_documentation else []

    latest_writers = WritersTeam.objects.filter(year__year=selected_year).first()
    assistants_writers = latest_writers.assistants.all() if latest_writers else []

    latest_multimedia = MultimediaTeam.objects.filter(year__year=selected_year).first()
    assistants_multimedia = latest_multimedia.assistants.all() if latest_multimedia else []

    latest_esports = EsportsTeam.objects.filter(year__year=selected_year).first()
    assistants_esports = latest_esports.assistants.all() if latest_esports else []
    
    latest_social_media = SocialMediaTeam.objects.filter(year__year=selected_year).first()
    assistants_social_media = latest_social_media.assistants.all() if latest_social_media else []
    
    latest_marketing = MarketingTeam.objects.filter(year__year=selected_year).first()
    assistants_marketing = latest_marketing.assistants.all() if latest_marketing else []
    
    latest_banner = ExecutiveBanner.objects.filter(year__year=selected_year).first()
    
    latest_advisers = Adviser.objects.filter(year__year=selected_year)

    
    latest_board_members = BoardMember.objects.filter(year__year=selected_year)
    
    about_us_context = AboutUsContext.objects.first()
    
    vision_mission_goal = VisionMissionGoal.objects.first()

    context = {
        'year': latest_year,
        'latest_executives': latest_executives,
        'latest_documentation': latest_documentation,
        'assistants_docu': assistants_docu,
        
        'latest_programming': latest_programming,
        'assistants_prog': assistants_prog,
        
        'latest_writers': latest_writers,
        'assistants_writers': assistants_writers,
        
        'latest_multimedia': latest_multimedia,
        'assistants_multimedia': assistants_multimedia,
        
        'latest_esports': latest_esports,
        'assistants_esports': assistants_esports,
        
        'latest_social_media': latest_social_media,
        'assistants_social_media': assistants_social_media,
        
        'all_years': all_years, 
        
        'latest_banner':latest_banner,
        'selected_year': selected_year,
        
        'about_us_context':about_us_context,
        'vision_mission_goal': vision_mission_goal,
        
        'latest_marketing':latest_marketing,
        'assistants_marketing': assistants_marketing,
        
        'latest_board_member':latest_board_members,
        
        'latest_adviser':latest_advisers,
        
        
    }
    
    return render(request, 'about_us.html', context)

def membership(request):
    september = ""
    january = ""
    subscription_status = ""
    date_now = timezone.now()
    sub = 0
    
    if request.user.is_authenticated:
        current_time = timezone.now()
        user_register_1 = request.user.sem_1
        user_register_2 = request.user.sem_2

        if (user_register_1 and user_register_1 > current_time) and \
           (user_register_2 and user_register_2 > current_time):
            sub = 1 
            subscription_status = "Both semesters are active."
        elif user_register_1 and user_register_1 > current_time:
            sub = 3  
            subscription_status = "First semester is active."
        elif user_register_2 and user_register_2 > current_time:
            sub = 4  
            subscription_status = "Second semester is active."
        else:
            sub = 2 
            subscription_status = "No active semesters."
 
    current_month = datetime.now().month
    if current_month in [1, 2, 3, 4, 5, 6, 7, 8]:
        january = "This is the second semester. Register now!"
    elif current_month in [9, 10, 11, 12]:
        september = "This is the first semester. Register now!"
    print(current_month)
    return render(request, 'membership.html', {
        'september': september,
        'january': january,
        'subscription_status': subscription_status,
        'date_now': date_now,
        'sub': sub
    })

def sem_1_add(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.sem_1 is None:
        user.sem_1 = timezone.now() + timedelta(days=4*30) 
    else:
        user.sem_1 += timedelta(days=4*30)  
    user.save()
    login = request.build_absolute_uri(reverse('login-user'))
    formatted_sem_1_date = user.sem_1.strftime('%B %d, %Y')
    subject = 'Account Registration Completed'
    message = f'Your account has been registered valid until {formatted_sem_1_date}. <a href={login}>Login Now</a>'
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list, html_message=message)
    
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
    
    login = request.build_absolute_uri(reverse('login-user'))
    formatted_sem_2_date = user.sem_2.strftime('%B %d, %Y')
    subject = 'Account Registration Completed'
    message = f'Your account has been registered valid until {formatted_sem_2_date}. <a href={login}>Login Now</a>'
    recipient_list = [user.email]
    send_mail(subject, message, None, recipient_list, html_message=message)
    
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
    payment = Payment.objects.all()[0]
    return render(request, 'gcash_payment/gpayment.html',{'payment':payment})



def submit_ticket(request):
    return redirect('https://github.com/mj4w/ICPEPWebsite2024/issues')