# Generated by Django 4.1.7 on 2023-04-10 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope_api', '0006_alter_horoscope_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horoscope',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 10)),
        ),
    ]
