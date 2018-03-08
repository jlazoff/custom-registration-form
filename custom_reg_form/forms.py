from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cover_letter_file'].error_messages = {
            "required": u"Please upload a cover letter.",
            "invalid": u"We're pretty sure you made that up.",
        }
        self.fields['resume_file'].error_messages = {
            "required": u"Please upload your resume in PDF format.",
            "invalid": u"Please upload your resume in PDF format.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('user_race','linkedin_url','github_url','cover_letter_file','resume_file')