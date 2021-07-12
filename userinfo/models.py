from django.db import models

class UserContacts(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    question = models.TextField()
