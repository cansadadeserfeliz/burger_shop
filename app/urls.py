#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
