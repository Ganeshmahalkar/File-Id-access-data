from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import FileMetadata
from .serializers import FileMetadataSerializer

class FileMetadataViewSet(viewsets.ViewSet):
    def retrieve(self, request, file_id):
        try:
            entry = FileMetadata.objects.get(file_id=file_id)
            serializer = FileMetadataSerializer(entry)
            return Response(serializer.data)
        except FileMetadata.DoesNotExist:
            return Response({'message': 'Entry not found'}, status=404)
