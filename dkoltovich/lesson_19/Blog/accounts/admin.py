from django.contrib import admin
from django.contrib.auth.models import User

@admin.register(User)
class AdminBlog(admin.ModelAdmin):
    list_display = ('username' )
    search_fields = ('username')
