# Create your views here.
from django.shortcuts import get_object_or_404

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

    def post(self, request, *args, **kwargs):
        todo = request.data.get('todo')
        serializer = ItemSerializer(data=todo)
        if serializer.is_valid(raise_exception=True):
            todo_saved = serializer.save()

        return Response({"success": "Item '{}' created successfully".format(todo_saved.title)})

    def patch(self, request, pk, *args, **kwargs):
        return self.markCompleted(True, pk, *args, **kwargs)

    def markCompleted(self, completed, pk, *args, **kwargs):
        obj = get_object_or_404(Item, pk=pk)
        obj.completed = completed
        obj.save()

        return Response({"Marked : {}".format(completed)})
