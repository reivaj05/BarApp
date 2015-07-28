from django.core.urlresolvers import reverse
from django.views.generic import(
    CreateView, DeleteView, DetailView,
    ListView, TemplateView, UpdateView,
)
from .forms import MenuCreateForm, MenuUpdateForm
from .models import Menu
from common.mixins import (
    FormMessagesMixin, DoesExistMixin,
    LoginRequiredMixin, PermissionRequiredMixin
)

from .mixins import HandleVenueMixin

# Create your views here.


class IndexView(TemplateView):
    template_name = 'menus/index.html'


class MenuDetailView(
        LoginRequiredMixin, DoesExistMixin,
        HandleVenueMixin, DetailView):
    template_name = 'menus/menu_detail.html'
    model = Menu


class MenuDeleteView(
        LoginRequiredMixin, FormMessagesMixin, DoesExistMixin,
        HandleVenueMixin, DeleteView):
    template_name = 'menus/menu_delete.html'
    model = Menu

    def get_success_url(self):
        return reverse('menus:menu_list', kwargs={'venue_id': self.venue.id})


class MenuListView(LoginRequiredMixin, HandleVenueMixin, ListView):
    template_name = 'menus/menu_list.html'
    context_object_name = 'menu_list'
    model = Menu

    def get_queryset(self):
        return Menu.objects.filter(venue=self.kwargs['venue_id'])


class MenuCreateView(
        LoginRequiredMixin,  # PermissionRequiredMixin,
        FormMessagesMixin, HandleVenueMixin, CreateView):
    template_name = 'menus/menu_create.html'
    form_class = MenuCreateForm
    # permission = 'menus.add_menu'
    success_message = 'Menu successfully created'
    error_message = 'There was an error trying to create the menu'

    def get_success_url(self):
        return reverse('menus:menu_list', kwargs={'venue_id': self.venue.id})

    def get_form_kwargs(self):
        kwargs = super(MenuCreateView, self).get_form_kwargs()
        kwargs.update({
            'venue': self.venue
        })
        return kwargs


class MenuUpdateView(
        LoginRequiredMixin, FormMessagesMixin, DoesExistMixin,
        HandleVenueMixin, UpdateView):
    template_name = 'menus/menu_update.html'
    form_class = MenuUpdateForm
    model = Menu
    success_message = 'Menu successfully updated'
    error_message = 'An error ocurred trying to update the menu'

    def get_success_url(self):
        return reverse(
            'menus:menu_detail',
            kwargs={
                'venue_id': self.venue.id,
                'pk': self.kwargs['pk'],
            }
        )
