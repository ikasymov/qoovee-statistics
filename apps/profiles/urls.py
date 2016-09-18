# coding: utf-8
from django.conf.urls import url
from apps.profiles import views


urlpatterns = [
    url(r'^(?P<edit_profile_id>[0-9]+)/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<profiles_id>[0-9]+)/profiles/$', views.detail_info, name='profile'),
]
