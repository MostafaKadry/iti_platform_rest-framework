from django.urls import path
from .views import TrackListCreateApiView, TrackDetailApiView

urlpatterns = [
    path('', TrackListCreateApiView, name='track-list-create'),
    path('<int:pk>/', TrackDetailApiView, name='track-detail'),
]