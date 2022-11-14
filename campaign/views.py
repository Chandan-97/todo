# Create your views here.
from django.shortcuts import get_object_or_404

from .models import Campaign
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CampaignSerializer


class CampaignView(APIView):
    def get(self, request, *args, **kwargs):
        todos = Campaign.objects.filter(is_deleted=False).all()
        resp = {
            "data": CampaignSerializer(todos, many=True).data
        }

        return Response(resp)

    def post(self, request, *args, **kwargs):
        campaign = request.data.get('data')
        serializer = CampaignSerializer(data=campaign)
        if serializer.is_valid(raise_exception=True):
            campaign_obj = serializer.save()

        return Response({"success": "Campaign '{}' created successfully".format(campaign_obj.name)})

    def patch(self, request, pk, *args, **kwargs):
        return self.markCompleted(True, pk, *args, **kwargs)

    def markCompleted(self, completed, pk, *args, **kwargs):
        obj = get_object_or_404(Campaign, pk=pk)
        obj.completed = completed
        obj.save()

        return Response({"Marked : {}".format(completed)})

