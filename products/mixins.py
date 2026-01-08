from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.utils.decorators import method_decorator
from django.http import Http404

class StaffRequiredMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(StaffRequiredMixin, cls).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(*args, **kwargs)
        return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class FilterMixin(object):
    filterset_class = None
    search_ordering_param = 'ordering'

    def get_queryset(self, *args, **kwargs):
        try:
            qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
            filterset_class = self.filterset_class
            if filterset_class:
                fs = filterset_class(self.request.GET, queryset=qs)
                return fs.qs
            else:
                return qs
        except:
            raise ImproperlyConfigured('You must have a queryset in order to use the FilterMixin')

    def get_context_data(self, *args, **kwargs):
        context = super(FilterMixin, self). get_context_data(*args, **kwargs)
        qs = self.get_queryset(*args, **kwargs)
        ordering = self.request.GET.get(self.search_ordering_param)
        if ordering:
            qs = qs.order_by(ordering)
        filterset_class = self.filterset_class
        if filterset_class:
            fs = filterset_class(self.request.GET, queryset=qs)
            context['object_list'] = fs.qs
        return context
