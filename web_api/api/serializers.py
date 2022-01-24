from rest_framework import serializers
from api.models import Property

PROPERTY_FIELDS = ['externalId', 'areaSqm','isRoomActive',
                  'roomMates', 'rent',
                  'deposit','additionalCost', 'registrationCost',
                  'costPerSqm', 'city', 'latitude', 'longitude',
                  'postalCode']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


