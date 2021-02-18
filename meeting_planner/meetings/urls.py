from django.urls import path
from . import views
from .views import detail, rooms

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms, name='rooms'),
    path('new', views.new, name='new'),
]
