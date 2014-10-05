from django.shortcuts import render, get_object_or_404
from .models import Ship


def details(request, ship_id):
    d = {}
    d['ship'] = get_object_or_404(Ship, pk=ship_id)
    return render(request, 'ship/details.html', d)

# EOF
