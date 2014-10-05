#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone = models.CharField(
        verbose_name=u'phone',
        max_length=25,
        validators=[RegexValidator(
            r'^((\+\d{1,2}){0,1})(\(\d{1,3}\)){0,1}(\d{6,7})$',
            u'For example, +57(1)1234567.',
            u'Phone number is not valid.'
        )],
        blank=True,
    )

    address = models.CharField(
        verbose_name=u'address',
        max_length=256,
    )

    delivery_info = models.TextField(
        verbose_name=u'delivery details',
    )


