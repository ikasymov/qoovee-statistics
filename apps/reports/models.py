# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from apps.profiles.models import Profile


class Department(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=150, default=None)

    def __unicode__(self):
        return self.name


class Report(models.Model):
    user = models.ForeignKey(Profile, related_name='profile')
    department = models.ForeignKey(Department, related_name='report')
    created_date = models.DateTimeField(default=timezone.now())
    edited_by = models.ForeignKey(User)
    edited_at = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.department.name

    class Meta:
        verbose_name = _('Отчет')
        verbose_name_plural = _('Отчеты')


class Statistic(models.Model):
    name = models.CharField(max_length=90)
    value = models.IntegerField()
    report = models.ForeignKey(Report, related_name='stat_report')

    def __unicode__(self):
        return self.name
