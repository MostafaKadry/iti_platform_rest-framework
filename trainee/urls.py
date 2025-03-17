from django.urls import path
from .views import TraineeListCreateAPIView, TraineeDetailAPIView

urlpatterns = [
    path('', TraineeListCreateAPIView.as_view(), name='trainee-list-create'),
    path('<int:pk>/', TraineeDetailAPIView.as_view(), name='trainee-detail'),
]