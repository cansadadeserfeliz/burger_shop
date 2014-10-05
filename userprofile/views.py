#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Vera Mazhuga http://vero4ka.info
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from userprofile.forms import UserForm

from braces.views import LoginRequiredMixin


User = get_user_model()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(
            self.request,
            u'Your contact information was updated successfully',
        )
        return super(UserUpdateView, self).form_valid(form)