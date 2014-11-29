from rest_framework import serializers
from . import models


class Entry(serializers.ModelSerializer):

    class Meta:
        model = models.Entry
