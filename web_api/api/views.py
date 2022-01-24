from api.models import Property
from api.serializers import PropertySerializer
from rest_framework import generics


# https://www.youtube.com/watch?v=Ue52N-eu9MM APIViews

# Create your views here.

class PropertyList(generics.ListCreateAPIView):
    """
    Retrieves and updates a list of all the properties or with a certain longitude and latitude.

        Is it just me or is this vague

        "to retrieve, update, and delete all properties with the same longitude and
        latitude;"
    """
    serializer_class = PropertySerializer

    def get_queryset(self):
        queryset = Property.objects.all()
        # Filtering on longitude and latitude
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')
        if longitude is not None:
            queryset = queryset.filter(longitude=longitude)
        elif latitude is not None:
            queryset = queryset.filter(latitude=latitude)
        return queryset


class _property(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, retrieves and deletes specific property by its externalId
    """
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    lookup_field = 'externalId'


class City(generics.ListAPIView):
    """
    Retrieves all properties in a city where isRoomActive = True optionally filtered and within a rent budget
    """
    serializer_class = PropertySerializer

    def get_queryset(self):
        city = self.kwargs['city']
        numResults = 10
        # Check if number of results is specified
        if self.request.query_params.get('num-results') is not None:
            numResults = int(self.request.query_params.get('num-results'))

        queryset = Property.objects.filter(city=city)

        # isRoomActive = self.request.query_params.get('isRoomActive')
        # Getting filtering parameters form the URL
        minRent = self.request.query_params.get('min-rent')
        maxRent = self.request.query_params.get('max-rent')

        # Checking if they are present
        if minRent is not None:
            queryset = queryset.filter(rent__gte=minRent)

        if maxRent is not None:
            queryset = queryset.filter(rent__lte=maxRent)

        return queryset[:numResults]
