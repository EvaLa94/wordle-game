from rest_framework import serializers
from .models import FiveCharWord


class FiveCharWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiveCharWord
        fields = '__all__'
