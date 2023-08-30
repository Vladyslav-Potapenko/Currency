from django.conf import settings
from django.core.mail import send_mail
from django.http.response import HttpResponse, HttpResponseRedirect, Http404   # noqa F401
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DetailView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from currency.models import Rate, Contact_us, Source
from currency.forms import RateForm, SourceForm, ContactusForm


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


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


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


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


class ContactusListView(ListView):
    queryset = Contact_us.objects.all()
    template_name = 'contact_us.html'


class ContactusCreateView(CreateView):
    form_class = ContactusForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus')

    def _send_mail(self):
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User Contact Us'
        body = f'''
                Email to reply: {self.object.email_from}.
                Subject Subject: {self.object.subject}.
                Body: {self.object.message}.
                '''
        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False
        )

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
