from django.conf import settings
from django.db import models
#from .ContentTypeRestrictedFileField import ContentTypeRestrictedFileField

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Set Upload Path to uploads/resumes/{user_id}.{filename}.{DateTime}.{ext}
def upload_resume_to(instance, filename):
     return 'resumes/user_{0}/{1}'.format(instance.user.id, filename)

class ExtraInfo(models.Model):
    """
    This model contains four extra fields to registration:

    User Race - Text Field
    GitHub URL - Text Field
    Cover Letter - Text Field
    Resume - File Upload

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
    cover_letter_file = models.CharField(
        verbose_name="Cover Letter",
        blank=True, 
        max_length=3000,
    )
    resume_file = models.FileField(
        upload_to=upload_resume_to,
        blank = True,
        null = True,
    )