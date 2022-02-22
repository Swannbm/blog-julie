from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "is_staff",
        "is_active",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    fieldsets = (
        (
            None,
            {"fields": ("first_name", "last_name", "email", "organism", "function")},
        ),
        (
            "Password",
            {"fields": ("password",)},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "organism",
                    "function",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
