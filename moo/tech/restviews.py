from rest_framework import generics
from .models import Tech
from .serializers import TechSerializer


class TechList(generics.ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class TechDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

# EOF
