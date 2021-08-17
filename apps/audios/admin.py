from django.contrib import admin

from apps.audios.models import Category, Audio

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'picture', 'audio_file']
