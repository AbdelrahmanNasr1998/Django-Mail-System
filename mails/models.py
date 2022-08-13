from django.db import models
from accounts.models import Accounts
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

CHOICES = (
    ('0', 'بريد صادر'),
    ('1', 'بريد محفوظ'),
)

class Mail(models.Model):
    From = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='من', related_name='From')
    To = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='إلى', related_name='To')
    Sub = models.CharField(max_length=128, verbose_name='العنوان')
    Msg = RichTextUploadingField(verbose_name='محتوي البريد')
    Date = models.DateTimeField(default=timezone.now, verbose_name='التاريخ')
    Draft = models.CharField(max_length=8, choices=CHOICES, verbose_name="صادر - حفظ", default=0)
    Seen = models.BooleanField(default=False)
    Mailid = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'E-Mail'
        verbose_name_plural = 'E-Mails'



class Attachments(models.Model):
    Mailid = models.PositiveBigIntegerField()
    Mailfrom = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='من', related_name='Mailfrom', blank=True, null=True)
    Mailto = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='إلى', related_name='Mailto', blank=True, null=True)
    Attachment = models.FileField(upload_to="Attachment", blank=True, verbose_name='المرفقات')
    Date = models.DateTimeField(default=timezone.now, verbose_name='التاريخ')

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'