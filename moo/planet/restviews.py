from rest_framework import generics
from .models import Planet
from .serializers import PlanetSerializer


class PlanetList(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class PlanetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

# EOF
