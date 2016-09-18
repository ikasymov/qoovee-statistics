# coding: utf-8
from django.contrib import admin
from apps.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Общая информация', {'fields': ['user', 'first_name', 'last_name', 'department', 'sex', 'position']}),
        ('Контактные данные', {'fields': ['phone']}),
        ('Фото профиля', {'fields': ['photo']}),
        ]
    list_display = ('first_name', 'last_name', 'date_of_birth', 'sex', )


admin.site.register(Profile, ProfileAdmin)
