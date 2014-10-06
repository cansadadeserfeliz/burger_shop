#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.views.generic import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.safestring import mark_safe

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
            mark_safe(
                u'Your order was created successfully. '
                u'<a href="{0}">'
                u'See a list of orders.'
                u'</a>'.format(
                    reverse('shop:order_list')
                ),
            ),
        )
        return HttpResponseRedirect(self.get_success_url())


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 5

    def dispatch(self, *args, **kwargs):
        # get the value of the filter by status
        self.status_query = self.request.GET.get('status', None)
        try:
            self.status_query = int(self.status_query)
        except (ValueError, TypeError):
            self.status_query = None
        return super(OrderListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        # filter by status of an order
        if self.status_query:
            queryset = queryset.filter(
                status=self.status_query,
            )
        # return orders of the current user
        return queryset.filter(
            created_by=self.request.user,
        )

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        # return the value of a filter by status in a context
        context['status_query'] = self.status_query
        return context