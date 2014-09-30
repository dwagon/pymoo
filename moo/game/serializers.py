from .models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    systems = serializers.RelatedField(many=True)

    class Meta:
        model = Game
        fields = ('turn', 'max_x', 'max_y', 'numplanets', 'systems')

# EOF
