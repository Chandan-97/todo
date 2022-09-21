# Create your views here.
from api.models import Item
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ItemSerializer


class ItemView(APIView):
    def get(self, request, *args, **kwargs):
        todos = Item.objects.filter(is_deleted=False).all()
        resp = {
            "data": ItemSerializer(todos, many=True).data
        }

        return Response(resp)
