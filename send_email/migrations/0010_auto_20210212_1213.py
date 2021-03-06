# Generated by Django 3.1.5 on 2021-02-12 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0009_auto_20210212_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 12, 12, 22, 1, 983385), verbose_name='Дата отправки'),
        ),
    ]
