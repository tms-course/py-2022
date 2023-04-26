# Generated by Django 4.1.5 on 2023-02-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_slug_alter_event_datetime_alter_event_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=256, unique=True, verbose_name='Slug'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['slug'], name='events_even_slug_30eb0f_idx'),
        ),
    ]