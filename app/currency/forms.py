from django import forms

from currency.models import Rate, Source, Contact_us


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'currency',
            'source'
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'phone',
            'logo'
        )


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = (
            'email_from',
            'subject',
            'message',
        )
