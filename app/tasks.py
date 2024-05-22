from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import HighlightsEvent
from django.contrib.auth.models import User

@shared_task
def send_highlight_email_task(event_id):
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
                'name': user.last_name if user.last_name else user.username,
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

        return {'success': True, 'message': 'Emails sent successfully'}
    except Exception as e:
        return {'success': False, 'message': str(e)}
