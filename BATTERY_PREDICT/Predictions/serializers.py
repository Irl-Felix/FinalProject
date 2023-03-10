
from rest_framework import serializers
from .models import Trip , SOH_Prediction,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class SOH_PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOH_Prediction
        fields = "__all__"



class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["trip_id","uuid","origin","destination","distance_meters","duration_sec","timestamp"]