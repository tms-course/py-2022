from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    
    add_fieldset = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': ('sex', 'birth_date',)
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        ('Custom fields', {
            'fields': ('sex', 'birth_date',)
        })
    )