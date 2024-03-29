# Generated by Django 4.1.7 on 2023-03-10 00:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('distance_meters', models.FloatField()),
                ('duration_sec', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='Predictions.user')),
            ],
        ),
        migrations.CreateModel(
            name='SOH_Prediction',
            fields=[
                ('prediction_id', models.AutoField(primary_key=True, serialize=False)),
                ('capacity', models.FloatField()),
                ('voltage_measured', models.FloatField()),
                ('current_measured', models.FloatField()),
                ('temperature_measured', models.FloatField()),
                ('current_load', models.FloatField()),
                ('voltage_load', models.FloatField()),
                ('time_duration', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='Predictions.user')),
            ],
        ),
    ]
