from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Student

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 'student':
        Student.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )
