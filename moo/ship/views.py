from django.shortcuts import render, get_object_or_404
from .models import Ship
from system.models import System


def details(request, ship_id):
    d = {}
    d['ship'] = get_object_or_404(Ship, pk=ship_id)
    return render(request, 'ship/details.html', d)


def setDestination(request, ship_id, dest_id):
    sh = get_object_or_404(Ship, pk=ship_id)
    sy = get_object_or_404(System, pk=dest_id)
    sh.destsystem = sy
    sh.save()
    return render(request, 'ship/details.html', {'ship': sh})

# EOF
