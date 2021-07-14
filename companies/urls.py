from django.urls import path
from rest_framework import routers

from companies import views

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=views.CompanyViewset, basename="companies")
