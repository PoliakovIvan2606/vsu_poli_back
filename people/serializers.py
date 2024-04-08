from rest_framework import serializers
from .models import Person, News, Departments

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
