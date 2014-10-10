from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Building


def details(request, building_id):
    d = {}
    d['building'] = get_object_or_404(Building, pk=building_id)
    return render(request, 'building/details.html', d)

# EOF
