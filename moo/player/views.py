from django.shortcuts import render, get_object_or_404
from .models import Player


def details(request, player_id):
    d = {}
    d['player'] = get_object_or_404(Player, pk=player_id)
    return render(request, 'player/details.html', d)

# EOF
