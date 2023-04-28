from django.contrib import admin
from .models import CustomerReview


@admin.register(CustomerReview)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'author', 'customer_review', 'creation_date',)
    #list_filter = ('status',)
    ordering = ('-creation_date',)
    #actions = [update_blogs_status]