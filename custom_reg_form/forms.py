from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cover_letter_text'].error_messages = {
            "required": u"Please tell us... ",
            "invalid": u"We're pretty sure you made that up.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('user_race', 'github_url','resume_text', 'cover_letter_text')
