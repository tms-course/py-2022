# Generated by Django 4.1.5 on 2023-01-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='img',
            field=models.ImageField(blank=True, upload_to='questions/images/'),
        ),
    ]
