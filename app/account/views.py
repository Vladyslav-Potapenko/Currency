from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, RedirectView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from account.forms import UserSignUpForm


class SignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = str(kwargs.pop('username'))

        user = get_user_model().objects.filter(username=username).only('id').first()
        if user is not None:
            user.is_active = True
            user.save(update_fields=['is_active'])
        # else:
        #     print('No user found')

        url = super().get_redirect_url(*args, **kwargs)
        return url


class ProfileView(LoginRequiredMixin, UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar'
    )

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('account:profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Your password was successfully updated!'))
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, _('Please correct the error below.'))
        return response
