from django.urls import path

from .views import ItemView

urlpatterns = [
    path('list', ItemView.as_view(), name='ItemView'),
]
