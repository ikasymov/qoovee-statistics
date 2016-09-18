# coding: utf-8
from django.conf.urls import url
from apps.accounts import views


urlpatterns = [
    url(r'^registrations/$', views.register, name='register'),
    url(r'^login/$', views.authentication, name='login'),
    url(r'^logout/$', views.auth_logout, name='logout'),
    url(r'^page_for_guest/$', views.page_for_guest, name='guest_page'),
]
