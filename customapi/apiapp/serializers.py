from rest_framework import serializers
from apiapp.models import Flights

class FlightSerialigers(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = "__all__"