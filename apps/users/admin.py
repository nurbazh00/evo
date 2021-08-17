from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'dob', 'gender', 'country',
        'city', 'get_avatar', 'date_joined',
        'is_active',
    )

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src={obj.avatar.url} width="100" />'
            )

        return '-'

    get_avatar.short_description = 'Фото'