from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from . import serializers
from rest_framework import filters
from ..models import Volunteer, ReportPeople, Country
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class Volunt(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Volunteer.objects.all().order_by('-pk')
    serializer_class = serializers.VolunteerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'country': ["icontains"],
        'city': ["icontains"],
        'address': ["icontains"],
        'date': ['gte', 'lte', 'exact'],
        "role": ["icontains"]
    }


class Report(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ReportPeople.objects.all().order_by('-pk')
    serializer_class = serializers.ReportPeopleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'country': ["icontains"],
        'city': ["icontains"],
        'address': ["icontains"],
        'date': ['gte', 'lte', 'exact']
    }


class ListCountry(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Country.objects.all().order_by('-pk')
    serializer_class = serializers.CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'country': ["icontains"],
    }
