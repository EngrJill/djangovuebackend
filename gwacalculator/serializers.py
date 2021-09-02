from rest_framework import serializers
from .models import Subjs

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjs
        fields = '__all__'