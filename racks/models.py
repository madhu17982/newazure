from django.db import models

class rack_Azure(models.Model):
    subject=models.CharField(max_length=250)
    explanation= models.TextField(null=True)
    tips_and_tricks=models.CharField(max_length=250)
    code = models.TextField(null=True)
