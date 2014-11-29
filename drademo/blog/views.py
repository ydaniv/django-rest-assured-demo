from rest_framework import viewsets
from . import models, serializers


class Entries(viewsets.ModelViewSet):

    queryset = models.Entry.objects.all()
    serializer_class = serializers.Entry
