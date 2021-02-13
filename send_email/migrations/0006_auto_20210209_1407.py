# Generated by Django 3.1.5 on 2021-02-09 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0005_auto_20210204_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус отправки'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 14, 15, 38, 954046), verbose_name='Дата отправки'),
        ),
    ]
