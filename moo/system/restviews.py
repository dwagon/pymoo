from rest_framework import generics, viewsets
from .models import System, SystemCategory
from .serializers import SystemSerializer, SystemCategorySerializer


class SystemCategoryList(generics.ListCreateAPIView):
    queryset = SystemCategory.objects.all()
    serializer_class = SystemCategorySerializer


class SystemCategoryDetail(viewsets.ReadOnlyModelViewSet):
    queryset = SystemCategory.objects.all()
    serializer_class = SystemCategorySerializer


class SystemList(generics.ListCreateAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class SystemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

# EOF
