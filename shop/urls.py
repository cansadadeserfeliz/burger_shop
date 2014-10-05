#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, url

from shop.views import OrderCreateView


urlpatterns = patterns('',
    # make an order
    url(
        r'^order/$',
        OrderCreateView.as_view(),
        name='order_create',
    ),
)