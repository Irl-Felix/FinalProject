from django.contrib import admin
from .models import User,Trip,SOH_Prediction
# Register your models here.
admin.site.register(User)
admin.site.register(Trip)
admin.site.register(SOH_Prediction)
