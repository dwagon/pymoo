from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, GameSize
from system.models import System
from player.models import Player


def new(request, size):
    gs = GameSize.objects.get(name=size)
    g = Game()
    g.size = gs
    g.save()
    g.makeGalaxy()
    return redirect('gameDetails', game_id=g.id)


def delete(request, game_id):
    gm = get_object_or_404(Game, pk=game_id)
    gm.delete()
    games = Game.objects.all()
    return render(request, 'base/index.html', {'games': games})


def details(request, game_id):
    d = {}
    d['game'] = get_object_or_404(Game, pk=game_id)
    d['systems'] = System.objects.filter(game=d['game'])
    d['players'] = Player.objects.filter(game=d['game'])
    return render(request, 'game/details.html', d)

# EOF
