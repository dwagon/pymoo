from .models import System, SystemCategory
from rest_framework import serializers


class SystemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemCategory
        fields = ('name', 'blockwarp', 'prob_nothing', 'prob_asteroid', 'prob_gasgiant', 'prob_planet', 'prob_existing')


class SystemCatField(serializers.RelatedField):
    def to_native(self, value):
        return value.name


class SystemSerializer(serializers.ModelSerializer):
    category = SystemCatField()
    planets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = System
        fields = ('name', 'category', 'x', 'y', 'planets')

# EOF
