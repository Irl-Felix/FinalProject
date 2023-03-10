from django.urls import path,include
from . import views


urlpatterns = [
    path('users/', views.UserList,name='userurl'),
    path('trips/',views.TripList,name = 'tripurl'),
    path('predictions/', views.SOH_PredictionList,name='predictionurl'),
]