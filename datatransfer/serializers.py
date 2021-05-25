from rest_framework import serializers
from .models import Appdata
from .models import Localization


class AppdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appdata
        fields = ('id', 'time',
                  'position_x', 'position_y', 'position_z',
                  'magnetic_x', 'magnetic_y', 'magnetic_z',
                  'rotation_x', 'rotation_y', 'rotation_z',
                  'acc_x', 'acc_y', 'acc_z',
                  'tracking_lost', 'user_id')


class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ('id', 'time', 'localization_x', 'localization_y')


