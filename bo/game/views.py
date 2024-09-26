from django.shortcuts import render
from game.serializers import GameSerializer
from rest_framework import viewsets
from game.models import Game

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class =GameSerializer
    permission_classes = []


