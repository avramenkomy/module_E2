from django import forms
from send_email.models import EmailMessage

class EmailMessageForm(forms.ModelForm):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}), label="Тема письма")
    message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Текст письма")
    delay = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Задержка отправки")
    to_send = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}), label="Кому")
    # status = forms.BooleanField(widget=forms.TextInput(attrs={"style": "display: none"}))

    class Meta:
        model = EmailMessage
        fields = ('subject', 'message', 'delay', 'to_send')

