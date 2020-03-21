from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Volunteer(models.Model):
    timestamp = models.DateTimeField(
        _("Get Current date and time "), auto_now_add=True)
    name = models.CharField(_("Name of the volunteer"),
                            blank=True, null=True, max_length=250)
    country = models.CharField(
        _("Country name of the volunteer"), blank=True, null=True, max_length=250)
    city = models.CharField(_("City name of the volunteer"),
                            blank=True, null=True, max_length=250)
    address = models.CharField(
        _("Address name of the volunteer"), blank=True, null=True, max_length=250)
    date = models.DateField(_("Date of register"),
                            auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("voulunteers")

    def __str__(self):
        return self.name


class ReportPeople(models.Model):
    email = models.CharField(_("Email of the person"),
                             blank=True, null=True, max_length=250)
    name = models.CharField(_("Name of the person"),
                            blank=True, null=True, max_length=250)
    country = models.CharField(
        _("Country of case"), blank=True, null=True, max_length=250)
    source = models.CharField(
        _("Source of case"), blank=True, null=True, max_length=250)
    city = models.CharField(_("City of case"),
                            blank=True, null=True, max_length=250)
    address = models.CharField(
        _("Address of case"), blank=True, null=True, max_length=250)
    info = models.CharField(
        _("Information of case deaths, recoveries, critical or other"), blank=True, null=True, max_length=250)
    date = models.DateField(_("Date of register"),
                            auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(
        _("Get Current date and time "), auto_now_add=True)

    class Meta:
        verbose_name = _("reportpeople")
        verbose_name_plural = _("reportpeoples")

    def __str__(self):
        return self.name
