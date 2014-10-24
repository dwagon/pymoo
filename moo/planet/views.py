from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Planet
from building.models import Building
from ship.models import ShipDesign


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


def constructBuilding(request, planet_id, build_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    building = get_object_or_404(Building, pk=build_id)
    planet.constructBuilding(building)
    return redirect('planetDetails', planet_id=planet_id)


def constructShip(request, planet_id, design_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    design = get_object_or_404(ShipDesign, pk=design_id)
    planet.constructShip(design)
    return redirect('planetDetails', planet_id=planet_id)

# EOF
