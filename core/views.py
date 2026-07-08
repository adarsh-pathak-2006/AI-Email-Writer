from django.shortcuts import render
from core.models import Email_DB
from django.contrib.auth.models import User
from core.serializers import EmailSerializer, AuthSerializer, DashboardSerializer
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from ai.output import email_output
from rest_framework.permissions import IsAuthenticated


class RegisterAPI(CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    serializer_class=AuthSerializer

class DashboardAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data=Email_DB.objects.filter(user=self.request.user)
        serial=DashboardSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=DashboardSerializer(data=request.data)
        if serial.is_valid():
            recipent=serial.validated_data['recipent']
            purpose=serial.validated_data['purpose']
            tone=serial.validated_data['tone']
            length=serial.validated_data['length']
            output=email_output(recipent, tone, purpose, length)

            Email_DB.objects.create(user=self.request.user ,recipent=recipent, purpose=purpose, tone=tone, length=length, output=output)

            return Response(output)


class EmailDetailAPI(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=EmailSerializer

    def get_queryset(self):
        return Email_DB.objects.filter(user=self.request.user)



