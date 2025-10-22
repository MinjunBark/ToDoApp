from django.db import models
from django.utils import timezone

# Create your models here.
# class User(models.Model):
#     # fields
#     age = models.IntegerField()
#     name = models.CharField(max_length=100)
    

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    