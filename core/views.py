from django.shortcuts import render
from core.models import Email
from django.contrib.auth.models import User
from core.serializers import EmailSerializer, OutputSerializer, AuthSerializer, DashboardSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=AuthSerializer

class DashboardAPI(APIView):
    def get(self, request):
        data=Email.objects.filter(user=self.request.user)
        serial=DashboardSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=DashboardSerializer(data=request.data)
        if serial.is_valid():
            recipent=serial.validated_data['recipent']
            purpose=serial.validated_data['purpose']
            tone=serial.validated_data['tone']
            length=serial.validated_data['length']


class EmailDetailAPI(RetrieveAPIView):
    serializer_class=EmailSerializer

    def get_queryset(self):
        return Email.objects.filter(user=self.request.user)



