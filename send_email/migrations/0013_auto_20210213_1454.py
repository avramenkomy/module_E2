# Generated by Django 3.1.6 on 2021-02-13 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0012_auto_20210213_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 13, 15, 2, 37, 901827), verbose_name='Дата отправки'),
        ),
    ]