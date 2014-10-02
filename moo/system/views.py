from django.shortcuts import render, get_object_or_404
from .models import System
from planet.models import Planet


def details(request, system_id):
    d = {}
    d['system'] = get_object_or_404(System, pk=system_id)
    d['planets'] = Planet.objects.filter(system=d['system'])
    return render(request, 'system/details.html', d)

# EOF
