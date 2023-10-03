from rest_framework import viewsets

from currency.api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.models import Rate, Source, Contact_us
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as alias_filters
from rest_framework import filters

# from rest_framework import filters as rest_framework_filters

from app.currency.api.v1.paginators import RatePagination, SourcePagination, ContactUsPagination
from currency.api.v1.filters import RateFilter, SourceFilter, ContactUsFilter


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatePagination
    filter_backends = (
        alias_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('buy', 'sell', 'created')


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('-id')
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcePagination
    filter_backends = (
        alias_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ['name', 'code_name']
    filterset_class = SourceFilter
    ordering_fields = ('id',)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = Contact_us.objects.all().order_by('-id')
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = ContactUsPagination
    filter_backends = (
        alias_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = ContactUsFilter
    ordering_fields = ('id',)
