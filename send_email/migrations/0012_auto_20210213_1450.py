# Generated by Django 3.1.6 on 2021-02-13 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0011_auto_20210212_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 13, 14, 58, 54, 168909), verbose_name='Дата отправки'),
        ),
    ]
