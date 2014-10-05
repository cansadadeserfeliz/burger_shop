#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.conf.urls import patterns, url

from shop.views import OrderCreateView
from shop.views import OrderListView


urlpatterns = patterns('',
    # make an order
    url(
        r'^order/$',
        OrderCreateView.as_view(),
        name='order_create',
    ),

    # users oders
    url(
        r'^orders/$',
        OrderListView.as_view(),
        name='order_list',
    ),
)