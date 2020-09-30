from rest_framework import serializers

from .models import Auth

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'auther', 'age', 'created_at','update_at')
        model = Auth


