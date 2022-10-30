from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import *
from .models import *
from .utils import *


class DshHome(DataMixin, ListView):
    model = Dsh
    template_name = 'dsh/index.html'
    context_object_name = 'options'
    extra_context = {'title': 'Home'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        context.update(c_def)
        return context

    def get_queryset(self):
        return Dsh.objects.filter(available=True).select_related('cat')


class ShowOption(DataMixin, DetailView):
    model = Dsh
    template_name = 'dsh/option.html'
    slug_url_kwarg = 'option_slug'
    context_object_name = 'option'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['option'])
        context.update(c_def)
        return context
