from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Planet


def details(request, planet_id):
    d = {}
    d['planet'] = get_object_or_404(Planet, pk=planet_id)
    return render(request, 'planet/details.html', d)


def assignWorkers(request, planet_id, oldprof, newprof):
    planet = get_object_or_404(Planet, pk=planet_id)
    if oldprof not in ('W', 'S', 'F', 'U'):
        return HttpResponse("Unknown profession %s" % oldprof, status=500)
    if newprof not in ('W', 'S', 'F', 'U'):
        return HttpResponse("Unknown profession %s" % newprof, status=500)
    planet.reassignWorkers(oldprof, newprof)
    return redirect('planetDetails', planet_id=planet_id)

# EOF
