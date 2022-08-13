from django.contrib import admin
from .models import Mail, Attachments
# Register your models here.

class mailsAdmin(admin.ModelAdmin):
    model = Mail
    search_fields = ('From', 'To', 'Sub', 'Draft', 'Seen')
    list_filter = ('From', 'To', 'Sub', 'Draft', 'Seen')
    list_display = ('From', 'To', 'Sub', 'Draft', 'Seen')

admin.site.register(Mail, mailsAdmin)


class attachmentAdmin(admin.ModelAdmin):
    model = Attachments
    search_fields = ('Mailid', 'Mailfrom', 'Mailto', 'Attachment')
    list_filter = ('Mailid', 'Mailfrom', 'Mailto','Attachment')
    list_display = ('Mailid', 'Mailfrom', 'Mailto','Attachment')

admin.site.register(Attachments, attachmentAdmin)