from django.contrib import admin
from send_email.models import EmailMessage

# Register your models here.
@admin.register(EmailMessage)
class EmailMessageAdmin(admin.ModelAdmin):
    pass