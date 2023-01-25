from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Question

@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'img_preview',)

    def img_preview(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="40" />')