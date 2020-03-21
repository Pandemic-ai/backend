from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
import csv
from .models import infection, Transport

from django.conf import settings

# Register your models here.


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class ProfileAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'start_hour', 'end_hour', 'country', 'address', 'date', 'place_type', 'latitude',
                    'longitude', 'info']
    search_fields = ('location', 'country', 'address', 'date')

    actions = ["export_as_csv"]


class TransportAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'departure_place', 'arrival_place', 'departure_country',
                    'arrival_country', 'transport_number', 'transport_mode', 'date', 'arrival_time']
    search_fields = ('arrival_place', 'departure_place')
    list_display_links = ('date', 'departure_place', 'arrival_place', 'departure_country',
                          'arrival_country')
    list_filter = ('transport_mode',)

    actions = ["export_as_csv"]


# admin.site.register(AdminUser, VenueAdmin)
admin.site.register(infection, ProfileAdmin)
admin.site.register(Transport, TransportAdmin)
