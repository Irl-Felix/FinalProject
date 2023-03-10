from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        # return f'{self.first_name} {self.last_name} - {self.uuid}'

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    uuid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance_meters = models.FloatField()
    duration_sec = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.uuid} - Trip from - ({self.origin} to {self.destination})'

class SOH_Prediction(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    uuid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    capacity = models.FloatField()
    voltage_measured = models.FloatField()
    current_measured = models.FloatField()
    temperature_measured = models.FloatField()
    current_load = models.FloatField()
    voltage_load = models.FloatField()
    time_duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.uuid} - at {self.timestamp}'