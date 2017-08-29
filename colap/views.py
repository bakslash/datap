from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from colap.models import Data
from colap.serializers import DataSerializer
# Create your views here.
class DataViewSet(viewsets.ModelViewSet):
	#this function fetches rows of data in Data  table
	queryset = Data.objects.all()
	serializer_class = DataSerializer