from rest_framework.serializers import ModelSerializer
from core.models import Email_DB
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
        model=Email_DB
        fields='__all__'


class DashboardSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Email_DB
        fields=['user', 'id', 'recipent', 'purpose', 'tone', 'length', 'time']