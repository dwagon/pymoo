from rest_framework import generics
from .models import Ship
from .serializers import ShipSerializer


class ShipList(generics.ListCreateAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ShipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

# EOF
