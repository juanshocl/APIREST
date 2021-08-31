from rest_framework import serializers
from .models import Persona
from django.contrib.auth.models import User

# class PersonaSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.Serializer):
    class Meta:
        # model = Persona
        # fields = (
        #     'id',
        #     'nombre',
        #     'apellido',
        # )
        model = User
        fields = ['url', 'username', 'email', 'groups']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id',
            'nombre',
            'apellido',
        )
