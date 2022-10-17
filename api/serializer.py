from rest_framework import serializers
from api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ("id", "title", "created_at", "completed")

    def get_created_at(self, obj):
        return obj.created_at.timestamp()
