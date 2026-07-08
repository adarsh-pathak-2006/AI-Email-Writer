from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    recipent=models.EmailField()
    purpose=models.TextField()
    tone=models.CharField(max_length=20, choices=[('PROFESSIONAL', 'Professional'), ('FRIENDLY AND CONVERSATIONAL', 'Friendly and Conversational'), ('EMPATHETIC AND SUPPORTIVE', 'Empathetic and Supportive'), ('HUMOUROUS AND PLAYFUL', 'Humorous and Playful'), ('DIRECT AND ASSERTIVE', 'Direct and Assertive')])
    length=models.PositiveIntegerField()
    output=models.TextField(null=True)

    def __str__(self):
        return self.user.first_name

