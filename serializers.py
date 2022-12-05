from rest_framework import serializers
from export.models import FoodSales

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodSales
        exclude = ('id', )