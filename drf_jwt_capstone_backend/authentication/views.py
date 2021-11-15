from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = RegistrationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
