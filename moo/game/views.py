from django.shortcuts import render, get_object_or_404
from .models import Game
from system.models import System
from player.models import Player


def makeGalaxy(request):
    g = Game()
    g.save()
    g.makeGalaxy()
    return render(request, 'base/index.html')


def details(request, game_id):
    d = {}
    d['game'] = get_object_or_404(Game, pk=game_id)
    d['systems'] = System.objects.filter(game=d['game'])
    d['players'] = Player.objects.filter(game=d['game'])
    return render(request, 'game/details.html', d)

# EOF
