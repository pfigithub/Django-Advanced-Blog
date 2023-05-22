from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ('Authentication', {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active", "groups", "user_permissions", "last_login")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_superuser", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)