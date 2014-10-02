from django.shortcuts import render, get_object_or_404
from .models import Planet


def details(request, planet_id):
    d = {}
    d['planet'] = get_object_or_404(Planet, pk=planet_id)
    return render(request, 'planet/details.html', d)

# EOF
