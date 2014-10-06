from .models import Ship
from rest_framework import serializers


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('name', 'owner', 'system', 'x', 'y', 'design', 'destsystem')

# EOF
