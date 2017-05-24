from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Contacts


@receiver(post_save, sender=Contacts)
def send_new_profile_email(sender, instance, **kwargs):
    try:
        if kwargs["created"]:
            send_mail('New message at Talaikis.com', \
                '{0} ({1}) wrote: {2}.\n\n'.format(instance.name, instance.email, instance.message), \
                settings.DEFAULT_FROM_EMAIL,
                settings.NOTIFICATIONS_EMAILS, \
                fail_silently=True)
    except:
        pass
