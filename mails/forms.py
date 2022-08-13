from django import forms
from .models import Mail, Attachments
from django.forms import ClearableFileInput

class NewMail(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('To', 'Sub', 'Msg', 'Draft')


class NewAttachments(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ('Attachment',)
        widgets = {
            'Attachment': ClearableFileInput(attrs={'multiple': True})
        }

    def __init__(self, *args, **kwargs):
        super(NewAttachments, self).__init__(*args, **kwargs)
        self.fields['Attachment'].required = False


class ReplyMail(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('Msg', 'Draft')