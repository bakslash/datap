from colap.models import Data
from rest_framework import serializers

class DataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Data
		fields = ('data_collector','name','location','date_added','favourite_drink',)