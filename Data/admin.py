from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
import csv
from .models import Volunteer, ReportPeople
from django.conf import settings


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


class VolunteerAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'name', 'country', 'city', 'address', 'date']
    search_fields = ('city', 'country', 'address')
    actions = ["export_as_csv"]


class ReportAdmin(ImportExportModelAdmin, ExportCsvMixin):
    list_display = ["pk", 'name', 'country',
                    'city', 'address', 'date', 'email', 'info']
    search_fields = ('city', 'country', 'address')
    actions = ["export_as_csv"]


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(ReportPeople, ReportAdmin)
