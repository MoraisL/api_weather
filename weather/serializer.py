from rest_framework import serializers
from .models import WeatherEntity

# Definition of the Serializer for the WeatherEntity entity
class WeatherEntitySerializer(serializers.Serializer):
    # Defining the fields of the Serializer
    temperature = serializers.IntegerField()
    date = serializers.CharField()
    city = serializers.CharField(required=False)  # The city field is optional
    atmosphericPressure = serializers.CharField(required=False)  # The atmosphericPressure field is optional
    humidity = serializers.CharField(required=False)  # The humidity field is optional
    weather = serializers.CharField(required=False)  # The weather field is optional

    # Method to create a new instance of WeatherEntity from validated data
    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    # Method to update an existing instance of WeatherEntity with new data
    def update(self, instance, validated_data):
        # Updating the instance fields with the validated data, if provided
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.date = validated_data.get('date', instance.date)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        return instance