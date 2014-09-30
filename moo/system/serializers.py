from .models import System, SystemCategory
from rest_framework import serializers


class SystemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemCategory
        fields = ('name', 'blockwarp', 'prob_nothing', 'prob_asteroid', 'prob_gasgiant', 'prob_planet', 'prob_existing')


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('name', 'category', 'x', 'y')

# EOF
