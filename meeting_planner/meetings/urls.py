from django.urls import path
from . import views
from .views import detail, rooms

urlpatterns = [
    path('meetings/<int:id>', detail, name='detail'),
    path('rooms', rooms, name='rooms'),
]
