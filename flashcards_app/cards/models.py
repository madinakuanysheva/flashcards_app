from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='cards')
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.question} - {self.answer}"

class GeneratedTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязываем к пользователю
    topic = models.CharField(max_length=255)  # Название темы
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания темы

    def __str__(self):
        return self.topic


class GeneratedCard(models.Model):
    topic = models.ForeignKey(GeneratedTopic, on_delete=models.CASCADE, related_name='cards')
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.question} - {self.answer}"