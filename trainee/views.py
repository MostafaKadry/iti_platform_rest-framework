from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Trainee
from .serializers import TraineeSerializer

# List all trainees & create a new trainee
class TraineeListCreateAPIView(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            courses_number = request.data.get("courses_number")
            trainee = serializer.save()
            trainee.active = trainee.check_pre_requisites(int(courses_number)) if courses_number.isdigit() else False
            trainee.save()
            return Response({"message": "Trainee created successfully", "active": trainee.active}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, and delete a single trainee
class TraineeDetailAPIView(APIView):
    def get(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        serializer = TraineeSerializer(trainee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        serializer = TraineeSerializer(trainee, data=request.data, partial=True)
        if serializer.is_valid():
            courses_number = request.data.get("courses_number")
            if courses_number is not None:
                trainee.active = trainee.check_pre_requisites(int(courses_number)) if courses_number.isdigit() else False
            serializer.save(active=trainee.active)
            return Response({"message": "Trainee updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        trainee.delete()
        return Response({"message": "Trainee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
