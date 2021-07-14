from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from companies import serializer, models


# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    serializer_class = serializer.CompanySerializer
    queryset = models.Company.objects.all().order_by("-last_updated")
    pagination_class = PageNumberPagination
