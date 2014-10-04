from .models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    systems = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    max_x = serializers.Field(source='size.max_x')
    max_y = serializers.Field(source='size.max_y')
    numsystems = serializers.Field(source='size.numsystems')

    class Meta:
        model = Game
        read_only_fields = ('turn', 'name', 'numplayers')
        exclude = ('size',)

# EOF
