from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import  SongSerializer
from .models import  Song
# Create your views here.

# class SingerViewSet(viewsets.ModelViewSet):
#     serializer_class = SingerSerializer
#     queryset = Singer.objects.all()


class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

