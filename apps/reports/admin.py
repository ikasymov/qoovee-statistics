# coding: utf-8
from django.contrib import admin
from apps.reports.models import Department, Report, Statistic


class StatisticAdmin(admin.StackedInline):
    model = Statistic


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Отчеты', {'fields': ['user', 'department', 'edited_at', 'edited_by']}),
        ]
    inlines = [StatisticAdmin]
    list_display = ('user', 'department', )
admin.site.register(Department)
admin.site.register(Report, ReportAdmin)
admin.site.register(Statistic)
