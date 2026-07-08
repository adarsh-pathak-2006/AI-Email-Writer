from django.urls import path
from core.views import DashboardAPI, EmailDetailAPI

urlpatterns = [
    path('email/', DashboardAPI.as_view(), name='email'),
    path('email/<int:pk>/', EmailDetailAPI.as_view(), name='email_individual'),
]
