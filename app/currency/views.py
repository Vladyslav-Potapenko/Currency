from django.http.response import HttpResponse, HttpResponseRedirect, Http404   # noqa F401
from django.shortcuts import render, get_object_or_404
#from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DetailView, DeleteView, TemplateView
)

from django.urls import reverse_lazy

from currency.models import Rate, Contact_us, Source

from currency.forms import RateForm, SourceForm, ContactusForm


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source-list')


class ContactusListView(ListView):
    queryset = Contact_us.objects.all()
    template_name = 'contact_us.html'


class ContactusCreateView(CreateView):
    form_class = ContactusForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus')


class ContactusUpdateView(UpdateView):
    model = Contact_us
    form_class = ContactusForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus')


class ContactusDetailView(DetailView):
    model = Contact_us
    template_name = 'contactus_details.html'


class ContactusDeleteView(DeleteView):
    model = Contact_us
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus')


class IndexView(TemplateView):
    template_name = 'index.html'