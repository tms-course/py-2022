# Generated by Django 4.1.5 on 2023-01-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_organizer_alter_event_attendees'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['name'], name='events_even_name_d5901c_idx'),
        ),
    ]
