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
            return super(HandleVenueMixin, self).dispatch(
                request, *args, **kwargs)
        except Venue.DoesNotExist:
            raise Http404('No Venue found matching the query')
