import django_filters

from currency.models import Rate, Source, Contact_us


class RateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sell': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'currency': ('exact',),
        }


class SourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Source
        fields = {
            'id': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'name': ('exact', 'iexact', 'contains', 'icontains'),
        }


class ContactUsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Contact_us
        fields = {
            'id': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'email_from': ('exact', 'iexact', 'contains', 'icontains'),
        }
