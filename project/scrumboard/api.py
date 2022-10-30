from rest_framework.viewsets import ModelViewSet
from scrumboard.serializers import ListSerializer, CardSerializer
from scrumboard.models import List, Card

"""
ModelViewSet allows GET PUT POST DELETE
"""

class ListViewSet(ModelViewSet):
    queryset = List.objects.all() # we collect all objects from db
    serializer_class = ListSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer