from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Metta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price']
        