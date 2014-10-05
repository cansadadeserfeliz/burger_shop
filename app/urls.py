#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    #url(r'^accounts/', include('django.contrib.auth.urls', namespace='userprofile')),
    url(r'^accounts/', include('userprofile.urls', namespace='userprofile')),

    url(r'^admin/', include(admin.site.urls)),
)
