from django.db import models

class users(models.Model):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username