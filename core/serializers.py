from rest_framework.serializers import ModelSerializer
from core.models import Email
from django.contrib.auth.models import User

class AuthSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email']

        
class EmailSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Email
        fields='__all__'

class OutputSerializer(ModelSerializer):
    class Meta:
        model=Email
        fields=['output']

class DashboardSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Email
        fields=['user', 'id', 'recipent', 'purpose', 'tone', 'length']