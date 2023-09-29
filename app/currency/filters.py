import django_filters

from currency.models import Rate, Source, Contact_us


class RateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'currency'
        )


class SourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Source
        fields = (
            'name',
            'source_url'
        )


class ContactusFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Contact_us
        fields = (
            'email_from',
            'subject'
        )
