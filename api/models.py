from django.db import models


# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
