from django.urls import path
from .views import (TraineeListCreateAPIView,
                    TraineeDetailAPIView,
                    SignInTraineeAPIView,
                    SignOutTraineeAPIView,
                    verify_email)

urlpatterns = [
    path('', TraineeListCreateAPIView.as_view(), name='trainee-list-create'),
    path('<int:pk>/', TraineeDetailAPIView.as_view(), name='trainee-detail'),
    path('login/', SignInTraineeAPIView.as_view(), name='trainee-login'),
    path('logout/', SignOutTraineeAPIView.as_view(), name='trainee-logout'),
    path('verfiy_email/', verify_email, name='verify-email'),
]