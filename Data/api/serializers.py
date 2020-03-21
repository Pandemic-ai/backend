from rest_framework import serializers
from ..models import Volunteer, ReportPeople


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"


class ReportPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportPeople
        fields = "__all__"

