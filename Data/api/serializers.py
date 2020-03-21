from rest_framework import serializers
from ..models import Volunteer, ReportPeople, Country


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"


class ReportPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportPeople
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    state = serializers.ListField(
        child=serializers.CharField(), source='state_as_list')

    class Meta:
        model = Country
        fields = "__all__"
