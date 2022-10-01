from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers


class MemberLoginrSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
