from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Summarie(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="Nenhum título adicionado.")
    text = models.TextField()

    def __str__(self):
        return self.title

