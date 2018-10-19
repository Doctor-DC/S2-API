from django.shortcuts import render

# Create your views here.

from s2.models import S2
from s2.serializers import S2Serializer

from rest_framework import viewsets


# Create your views here.
class S2ViewSet(viewsets.ModelViewSet):
    queryset = S2.objects.all()
    serializer_class = S2Serializer