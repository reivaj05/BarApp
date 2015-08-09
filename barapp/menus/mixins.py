from django.core.urlresolvers import reverse
from django.http import Http404
from venues.models import Venue


class HandleVenueMixin(object):

    def get_context_data(self, **kwargs):
        context = super(HandleVenueMixin, self).get_context_data(**kwargs)
        context['venue'] = self.venue
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            self.venue = Venue.objects.get(id=self.kwargs['venue_id'])
            self.no_permission_url = reverse(
                'menus:menu_list',
                kwargs={'venue_id': self.venue.id}
            )
            return super(HandleVenueMixin, self).dispatch(
                request, *args, **kwargs)
        except Venue.DoesNotExist:
            raise Http404('No Venue found matching the query')
