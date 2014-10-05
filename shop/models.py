#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Sum


class Ingredient(models.Model):
    name = models.CharField(
        max_length=36,
    )

    price = models.PositiveIntegerField()

    is_active = models.BooleanField(
        default=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        default=timezone.now,
    )

    def __unicode__(self):
        return u'{0} ({1}$)'.format(self.name, self.price)

    class Meta:
        ordering = ('name',)


class Order(models.Model):
    STATUS_ORDERED = 1
    STATUS_IN_PROGRESS = 2
    STATUS_ON_ROAD = 3
    STATUS_DELIVERED = 4
    STATUS_CHOICES = (
        (STATUS_ORDERED, u'ordered'),
        (STATUS_IN_PROGRESS, u'in progress'),
        (STATUS_ON_ROAD, u'on the road'),
        (STATUS_DELIVERED, u'delivered'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=u'user',
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=u'order date',
    )

    ingredients = models.ManyToManyField(
        'shop.Ingredient',
        limit_choices_to={'is_active': True},
    )

    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ORDERED,
    )

    @property
    def get_ingredients(self):
        return u', '.join(
            self.ingredients.all().values_list(
                'name',
                flat=True
            )
        )

    @property
    def get_price(self):
        return self.ingredients.aggregate(
            total_price=Sum('price'),
        )['total_price']

    def __unicode__(self):
        return u'{0}: {1}'.format(self.id, self.created_by)

    class Meta:
        ordering = ('-created_at',)
