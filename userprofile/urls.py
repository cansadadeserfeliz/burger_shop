#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login, logout

from userprofile.forms import CustomAuthenticationForm
from userprofile.views import UserUpdateView


urlpatterns = [
    # login
    url(
        r'^login/$',
        login,
        {
            'authentication_form': CustomAuthenticationForm,
        },
        name='login',
    ),

    # logout
    url(
        r'^accounts/logout/$',
        logout,
        {
            'next_page': reverse_lazy('home'),
        },
        name='logout',
    ),

    # profile settings
    url(
        r'^settings/$',
        UserUpdateView.as_view(),
        name='settings',
    ),
]