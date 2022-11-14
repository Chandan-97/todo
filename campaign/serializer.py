from rest_framework import serializers
from campaign.models import Campaign, CampaignEvent


class CampaignSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = ("id", "name", "start_time", "end_time", "status", "created_at")

    def get_created_at(self, obj):
        return obj.created_at.timestamp()


class CampaignEventSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    scheduled_at = serializers.SerializerMethodField()

    class Meta:
        model = CampaignEvent
        fields = ("id", "meta", "scheduled_at", "status", "created_at")

    def get_created_at(self, obj):
        return obj.created_at.timestamp()

    def get_scheduled_at(self, obj):
        return obj.scheduled_at.timestamp()
