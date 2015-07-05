from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from .forms import MenuCreateForm, MenuUpdateForm
from .models import Menu
from common import mixins

# Create your views here.


class IndexView(TemplateView):
    template_name = 'menus/index.html'


class MenuDetailView(DetailView):
    template_name = 'menus/detail_menu.html'
    model = Menu


class MenuCreateView(mixins.FormMessagesMixin, CreateView):
    template_name = 'menus/menu_create.html'
    form_class = MenuCreateForm
    success_message = 'Menu successfully created'
    error_message = 'There was an error trying to create the menu'


class MenuUpdateView(mixins.FormMessagesMixin, UpdateView):
    template_name = 'menus/menu_update.html'
    form_class = MenuUpdateForm
    success_message = 'Menu successfully updated'
    error_message = 'An error ocurred trying to update the menu'
