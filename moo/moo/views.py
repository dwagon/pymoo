from django.shortcuts import render
from game.models import Game, GameSize


def index(request):
    games = Game.objects.all()
    gamesizes = GameSize.objects.all()
    return render(request, 'base/index.html', {'games': games, 'sizes': gamesizes})

# EOF
