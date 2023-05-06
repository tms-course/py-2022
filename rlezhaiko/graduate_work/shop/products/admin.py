from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductImage, ProductReview


@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ('product', 'preview',)

    def preview(self, obj):
        if not obj.image:
            return 'unknown'

        return mark_safe(f"""<img src="{obj.image.url}" height="50"/>""")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 8


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'preview',)
    search_fields = ('name',)
    readonly_fields = ('preview',)
    inlines = [ProductImageInline]


    def preview(self, obj):
        if not obj.main_image:
            return 'unknown'

        return mark_safe(f"""<img src="{obj.main_image.url}" height="50" />""")


@admin.register(ProductReview)
class AdminProductReview(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'product_review', 'creation_date', 'status',)
    list_filter = ('status',)
    ordering = ('-creation_date',)