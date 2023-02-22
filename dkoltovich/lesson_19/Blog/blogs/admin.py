from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('title', 'description', 'creation_date', 'status', 'author', )
    search_fields = ('title', 'author__username', 'description')
    readonly_fields = ('creation_date',)
    ordering = ('-creation_date',)
    list_filter = ['status', 'creation_date', 'author']

