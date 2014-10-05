#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from userprofile.froms import CustomAuthenticationForm


urlpatterns = patterns('',
    # login
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {
            'authentication_form': CustomAuthenticationForm,
        },
        name='login',
    ),

    # logout
    url(
        r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': reverse_lazy('home'),
        },
        name='logout',
    ),
)