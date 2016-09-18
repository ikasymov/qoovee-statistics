# coding: utf-8
from django.conf.urls import url
from apps.reports import views


urlpatterns = [
    url(r'^add_report/$', views.add_report, name='add_report')
]
