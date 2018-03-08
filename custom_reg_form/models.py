from django.conf import settings
from django.db import models
from .ContentTypeRestrictedFileField import ContentTypeRestrictedFileField

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Set Upload Path to uploads/resumes/{user_id}.{filename}.{DateTime}.{ext}
def upload_resume_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)

    return 'uploads/resumes/user_{0}.{1}.{2}.{3}'.format(
        instance.user.id, 
        filename_base,   
        now().strftime("%Y%m%d%H%M"),
        filename_ext.lower()
    )

class ExtraInfo(models.Model):
    """
    This model contains four extra fields to registration:

    User Race - Text Field
    GitHub URL - Text Field
    Cover Letter - Text Field
    Resume - PDF Uploaded to default storage under `{user_id}.{filename}.{DateTime}.{ext}`

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
    resume_file = ContentTypeRestrictedFileField(
        upload_to=upload_resume_to,
        content_types=["application/pdf"],
        max_upload_size=10485760,
    )
    def __unicode__(self):
        return u"%s" % self.user