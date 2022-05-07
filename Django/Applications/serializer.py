from rest_framework import serializers

from Applications.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ("Name", "Email","Password","Mobile_No","Date_of_birth")