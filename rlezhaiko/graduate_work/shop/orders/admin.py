from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city',
                    'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
