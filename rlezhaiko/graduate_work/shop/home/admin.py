from django.contrib import admin
from .models import CustomerReview


@admin.register(CustomerReview)
class AdminCustomerReview(admin.ModelAdmin):
    list_display = ('id', 'author', 'customer_review', 'creation_date', 'status',)
    list_filter = ('status',)
    ordering = ('-creation_date',)