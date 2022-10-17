from django.urls import path

from .views import ItemView

urlpatterns = [
    path('list', ItemView.as_view(), name='ItemView'),
    path('completed/<int:pk>', ItemView.as_view(), name='ItemViewCompleted')
]
