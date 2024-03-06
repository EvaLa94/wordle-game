from rest_framework import serializers
from .models import FiveCharWord


class FiveCharWordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    word = serializers.CharField(max_length=5)
