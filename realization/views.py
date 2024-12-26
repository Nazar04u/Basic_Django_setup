from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from tutorial.quickstart.serializers import UserSerializer


class HomeView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
