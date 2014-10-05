#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from shop.models import Order
from shop.forms import OrderForm

from braces.views import LoginRequiredMixin


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        form.save_m2m()
        messages.success(
            self.request,
            u'Your order was created successfully',
        )
        return HttpResponseRedirect(self.get_success_url())


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user,
        )

