from django.shortcuts import render
from rest_framework import viewsets
from .models import Appdata
from .serializers import AppdataSerializer
from .models import Localization
from .serializers import LocalizationSerializer


class AppdataView(viewsets.ModelViewSet):
    queryset = Appdata.objects.all()
    serializer_class = AppdataSerializer


class LocalizationView(viewsets.ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer
