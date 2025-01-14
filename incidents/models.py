from django.db import models
import datetime


# Create your models here.
class Incident(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateTimeField(auto_now_add=False)
  status = models.CharField(max_length=255)
  message = models.TextField()

  def __str__(self):
    return f"{self.title} {self.status} {self.message}"