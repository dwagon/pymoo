from django.shortcuts import render, get_object_or_404
from .models import Tech


def details(request, tech_id):
    d = {}
    d['tech'] = get_object_or_404(Tech, pk=tech_id)
    return render(request, 'tech/details.html', d)

# EOF
