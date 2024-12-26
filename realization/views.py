from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import UserSerializer

class HomeView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Customization should happen here instead of overriding get()
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"result": serializer.data})


