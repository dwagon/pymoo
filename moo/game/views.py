from django.shortcuts import render
from .models import Game

def makeGalaxy(request):
    g = Game()
    g.save()
    g.makeGalaxy()
