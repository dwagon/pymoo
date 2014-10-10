from .models import Building
from rest_framework import serializers


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('name', 'cost', 'main', 'desc')

# EOF
