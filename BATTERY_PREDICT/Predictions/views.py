from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Trip,SOH_Prediction,User
from .serializers import TripSerializer,SOH_PredictionSerializer,UserSerializer


# Create your views here.
@api_view(['GET','POST'])
def SOH_PredictionList(request):
    if request.method == 'GET':
        predictions = SOH_Prediction.objects.all()
        predictionsserializer = SOH_PredictionSerializer(predictions, many=True)
        return Response(predictionsserializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        predictionsserializer = SOH_PredictionSerializer(data=request.data)
        if predictionsserializer.is_valid():
            predictionsserializer.save()
            return Response(predictionsserializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def TripList(request):
    trips = Trip.objects.all()
    tripserializer = TripSerializer(trips, many=True)
    return Response(tripserializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def UserList(request):
    user = User.objects.all()
    userserializer = UserSerializer(user, many=True)
    return Response(userserializer.data, status=status.HTTP_201_CREATED)
    # get all the trip 
    # serialize them
    # Return Json object