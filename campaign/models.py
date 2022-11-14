from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    meta = models.JSONField()
    sender = models.FilePathField(path=settings.MEDIA_ROOT)
    receiver = models.FilePathField(path=settings.MEDIA_ROOT)
    status = models.CharField(max_length=30, choices=(
        ("Completed", "COMPLETED"),
        ("In progress", "INPROGRESS"),
        ("Cancelled", "CANCELLED"),
        ("Failed", "FAILED")
    ))
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CampaignEvent(models.Model):
    campaign = models.ForeignKey(Campaign)
    meta = models.JSONField()
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=30, choices=(
        ("Completed", "COMPLETED"),
        ("Failed", "FAILED"),
        ("Pending", "PENDING"),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
