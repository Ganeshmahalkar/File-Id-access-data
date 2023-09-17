from rest_framework import serializers
from .models import MonetaryPenalty
from fileid.serializers import FileMetadataSerializer

class MonetaryPenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonetaryPenalty
        fields = '__all__' 