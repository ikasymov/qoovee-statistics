# coding: utf-8
from django.conf.urls import url
from apps.frontend import views


urlpatterns = [
    url(r'^$', views.index, name='main_page'),
]
