from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from send_email.models import EmailMessage
from send_email.forms import EmailMessageForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
import datetime
import time
import threading
from module_E2_HW import settings
from django.forms import formset_factory

# Create your views here.
threads = []

def sender(subject, message, from_mail, to_mails_list):
    mail = send_mail(subject, message, from_mail, to_mails_list, fail_silently=False)
    return mail


class MessageEdit(CreateView):
    model = EmailMessage
    form_class = EmailMessageForm
    success_url = reverse_lazy('send_email:message-edit')
    template_name = 'email_edit.html'


def message_create(request):
    if request.method == "POST":

        form = EmailMessageForm(request.POST)

        if form.is_valid():

            new_msg = form.save(commit=False)

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_mail = settings.EMAIL_HOST_USER
            to_mails_list = [form.cleaned_data['to_send']]

            delay = form.cleaned_data['delay']
            t = threading.Timer(delay, sender, args=(subject, message, from_mail, to_mails_list, ))
            threads.append(t)
            t.start()

            # mail = send_mail(subject, message, from_mail, to_mails_list, fail_silently=False)
            # if mail:
            #     new_msg.status = True
            # else:
            #     new_msg.status = False

            new_msg.send_date = new_msg.send_date_calc()
            new_msg.save()

            return redirect(reverse_lazy('send_email:message-edit'))

        else:
            # Обработка невалидной формы
            print("Ошибка формы")
            return redirect(reverse_lazy('send_email:message-edit'))
    else:
        form = EmailMessageForm()
    return render(request, 'email_edit.html', {"form": form})


def message_create_many(request):
    EmailMessageFormSet = formset_factory(EmailMessageForm, extra=3)
    if request.method == 'POST':
        email_formset = EmailMessageFormSet(request.POST, request.FILES, prefix='emails')
        if email_formset.is_valid():
            for email_form in email_formset:
                new_msg = email_form.save(commit=False)

                subject = email_form.cleaned_data['subject']
                message = email_form.cleaned_data['message']
                from_mail = settings.EMAIL_HOST_USER
                to_mails_list = [email_form.cleaned_data['to_send']]

                delay = email_form.cleaned_data['delay']

                t = threading.Timer(delay, sender, args=(subject, message, from_mail, to_mails_list,))
                threads.append(t)
                t.start()

                new_msg.send_date = new_msg.send_date_calc()
                new_msg.save()

            return redirect(reverse_lazy('send_email:message-create-many'))
    else:
        email_formset = EmailMessageFormSet(prefix='emails')
    return render(request, 'email_create_many.html', {"formset": email_formset})






class MessageList(ListView):
    model = EmailMessage
    queryset = EmailMessage.objects.all().order_by('-create_date')[:10]

class MessageDetail(DetailView):
    model = EmailMessage
    template_name = "send_email/message_detail.html"
