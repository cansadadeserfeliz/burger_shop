#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.contrib import admin

from shop.models import Ingredient
from shop.models import Order


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'created_by',
        'created_at',
        'is_active',
    )

    exclude = (
        'created_by',
        'created_at',
    )

    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        """User is saved automatically
        """
        obj.created_by = request.user

        super(
            IngredientAdmin,
            self
        ).save_model(
            request,
            obj,
            form,
            change,
        )

admin.site.register(Ingredient, IngredientAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'created_at',
    )

    fields = (
        'status',
    )

    def get_actions(self, request):
        actions = super(OrderAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Order, OrderAdmin)