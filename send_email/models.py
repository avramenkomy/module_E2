from django.db import models
import datetime


# Create your models here.
class EmailMessage(models.Model):
    subject = models.CharField(max_length=255, blank=False, verbose_name="Тема письма")
    message = models.TextField(verbose_name="Текст сообщения")
    delay = models.PositiveIntegerField(verbose_name="Задержка отправки")
    to_send = models.EmailField(verbose_name="Адресат")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # auto_now_add=True,
    send_date = models.DateTimeField(verbose_name="Дата отправки", default=datetime.datetime.now() + datetime.timedelta(seconds=500))
    status = models.BooleanField(verbose_name="Статус отправки", default=False)

    def send_date_calc(self):
        return datetime.datetime.now() + datetime.timedelta(seconds=self.delay)

    # def save(self, *args, **kwargs):
    #     self.send_date = self.send_date_calc()
    #     super(EmailMessage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    def __str__(self):
        return self.subject
