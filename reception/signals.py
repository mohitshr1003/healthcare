from django.db.models.signals import post_save
from healthcare.settings import EMAIL_HOST_USER
from .models import *
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=PatientDetail)
def send_email_confirmation(sender, instance, **kwargs):
    password = kwargs.get('pwd')

    if password:
        send_mail(
    subject='Healthcare Hospital registration confirmed.',
    message='''Thank you for your registration in Healthcare Hospital website. 
    Your User credentials are as following: 
    User ID: ''' + str(instance.patient_id) +
    '''
    Password: ''' + str(password),
    from_email=EMAIL_HOST_USER,
    recipient_list=[instance.patient_mail]
        )

@receiver(post_save, sender=DoctorDetail)
def send_email_confirmation(sender, instance, **kwargs):
    password = kwargs.get('pwd')

    if password:
        send_mail(
    subject='Healthcare Hospital registration confirmed.',
    message='''Thank you for your registration in Healthcare Hospital website. 
    Your User credentials are as following: 
    User ID: ''' + str(instance.doctor_id) +
    '''
    Password: ''' + str(password),
    from_email=EMAIL_HOST_USER,
    recipient_list=[instance.doctor_mail]
        )
