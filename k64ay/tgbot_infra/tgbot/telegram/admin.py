from django.contrib import admin
from telegram.models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('desc', 'user_id',)