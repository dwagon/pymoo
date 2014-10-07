from .models import Tech
from rest_framework import serializers


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ('name', 'categ', 'desc')

# EOF
