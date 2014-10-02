from django.shortcuts import render
from game.models import Game

import sys


def index(request):
    games = Game.objects.all()
    sys.stderr.write("games=%s\n" % games)
    return render(request, 'base/index.html', {'games': games})

# EOF
