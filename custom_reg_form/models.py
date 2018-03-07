from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
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
    resume_text = models.CharField(
        verbose_name="Resume",
        blank=True, 
        max_length=5000,
    )
     cover_letter_text = models.CharField(
        verbose_name="Cover Letter",
        blank=True, 
        max_length=5000,
    )
