from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin
from currency.models import Rate, Source, Contact_us


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'currency',
        'source',
        'created'
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter)
    )
    search_fields = (
        'buy',
        'sell',
        'source'
    )


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
        'phone'
    )
    list_filter = (
        'name',
    )


@admin.register(Contact_us)
class Contact_usAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message'
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
