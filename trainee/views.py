from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes

from .models import Trainee
from .serializers import TraineeSerializer
from .utiles import account_activation_token
from iti_platform_api.settings import EMAIL_HOST_USER

# List all trainees & create a new trainee
class TraineeListCreateAPIView(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():

#in front end required courses rendered and user check ones he knows and then front end send only number of courses
            courses_number = request.data.get("courses_number")
            trainee = serializer.save()
            trainee.is_active = trainee.check_pre_requisites(int(courses_number)) if courses_number.isdigit() else False
            trainee.save()

            try:
                # subject = 'Verfication Email'
                # message = render_to_string('mail_verfication.html', context={
                #     'user': trainee,
                #     'domain': request.get_host(),
                #     'uid': urlsafe_base64_decode(force_bytes(trainee.pk)),
                #     'token': account_activation_token.make_token(trainee)
                # })
                # send_mail(subject, message, EMAIL_HOST_USER, [trainee.email], fail_silently=False)
                return Response({"message": "Trainee created successfully", "active": trainee.active}, status=status.HTTP_201_CREATED)
            except:
                # trainee.delete()
                return Response({"message": "Fake email"}, status=status.HTTP_400_BAD_REQUEST)

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

# Signin Trainee