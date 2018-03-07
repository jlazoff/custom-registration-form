from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains four extra fields to registration
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
  
    user_race = models.CharField(
        verbose_name="Race",
        blank=True, 
        max_length=50,
    )
    github_url = models.CharField(
        verbose_name="Github URL",
        blank=True, 
        max_length=300,
    )
    resume_file = models.FileField(upload_to='not required sending to db')
    cover_letter_file = models.FileField(upload_to='not required sending to db')
