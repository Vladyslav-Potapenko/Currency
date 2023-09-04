from django.conf import settings
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect, Http404   # noqa F401
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, UpdateView,
    DetailView, DeleteView, TemplateView
)
from django_filters.views import FilterView
from currency.models import Rate, Contact_us, Source
from currency.forms import RateForm, SourceForm, ContactusForm
from currency.tasks import send_email_from_background

from app.currency.filters import RateFilter, SourceFilter, ContactusFilter


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')

    def get_queryset(self):
        queryset = Rate.objects.all()
        return queryset


class RateDetailView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'

    def get_queryset(self):
        queryset = Rate.objects.all()
        return queryset


class RateDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def get_queryset(self):
        queryset = Rate.objects.all()
        return queryset


class SourceListView(FilterView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')

    def get_queryset(self):
        queryset = Source.objects.all()
        return queryset


class SourceDetailView(LoginRequiredMixin, DetailView):
    model = Source
    template_name = 'source_details.html'

    def get_queryset(self):
        queryset = Source.objects.all()
        return queryset


class SourceDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')

    def get_queryset(self):
        queryset = Source.objects.all()
        return queryset


class ContactusListView(FilterView):
    queryset = Contact_us.objects.all()
    template_name = 'contact_us.html'
    paginate_by = 10
    filterset_class = ContactusFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class ContactusCreateView(CreateView):
    form_class = ContactusForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus')

    def _send_mail(self):
        recipient = settings.DEFAULT_FROM_EMAIL    # noqa F841
        subject = 'User Contact Us'
        body = f'''
                Email to reply: {self.object.email_from}.
                Subject Subject: {self.object.subject}.
                Body: {self.object.message}.
                '''
        send_email_from_background.delay(subject, body)

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class ContactusUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Contact_us
    form_class = ContactusForm # noqa F401
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus')


class ContactusDetailView(LoginRequiredMixin, DetailView):
    model = Contact_us
    template_name = 'contactus_details.html'


class ContactusDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = Contact_us
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus')


class IndexView(TemplateView):
    template_name = 'index.html'
