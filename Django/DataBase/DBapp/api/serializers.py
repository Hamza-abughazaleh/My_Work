from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from DBapp.models import Trip , AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id','username']

class TripCreateSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Trip
        fields = ['date','title','text']


class TripListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['date','title','text']

class TripDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id','text','date','title']
