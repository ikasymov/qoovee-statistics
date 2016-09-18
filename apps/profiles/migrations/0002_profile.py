# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=100, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_image', verbose_name='\u0424\u043e\u0442\u043e')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, verbose_name='\u0412\u044b\u0431\u043e\u0440 \u043f\u043e\u043b\u0430')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('position', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0444\u0438\u043b\u044c',
                'verbose_name_plural': '\u041f\u0440\u043e\u0444\u0438\u043b\u0438',
            },
        ),
    ]