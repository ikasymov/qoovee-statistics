# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
STATUS = (
    ('Active', 'Active'),
    ('Passive', 'Passive'),
)


class Profile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    user = models.OneToOneField(User, related_name='profile', verbose_name=_('Профиль'))
    phone = models.BigIntegerField(null=True, blank=True, verbose_name=_('Номер телефона'))
    photo = models.ImageField(upload_to='profile_image', verbose_name=_('Фото'), null=True, blank=True)
    sex = models.CharField(max_length=30, choices=GENDER, verbose_name=_('Выбор пола'))
    date_of_birth = models.DateField(null=True, blank=True)
    department = models.ForeignKey('reports.Department', related_name='departmant')
    position = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профили')
