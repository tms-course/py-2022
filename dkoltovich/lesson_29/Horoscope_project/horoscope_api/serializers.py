from rest_framework import serializers

from .models import Horoscope, Signs

class SignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signs 
        fields = ['name']

class HoroscopeSerializer(serializers.ModelSerializer):
    sign_name = SignsSerializer(many=False)
    class Meta:
        model = Horoscope 
        fields = ['sign_name', 'date', 'content',]
