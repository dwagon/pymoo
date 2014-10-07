from django.shortcuts import render, get_object_or_404
from .models import Player
from tech.models import Tech


def details(request, player_id):
    d = {}
    d['player'] = get_object_or_404(Player, pk=player_id)
    return render(request, 'player/details.html', d)


def setResearch(request, player_id, tech_id):
    d = {}
    d['player'] = get_object_or_404(Player, pk=player_id)
    d['tech'] = get_object_or_404(Tech, pk=tech_id)
    d['player'].researching = d['tech']
    d['player'].save()
    return render(request, 'player/details.html', d)

# EOF
