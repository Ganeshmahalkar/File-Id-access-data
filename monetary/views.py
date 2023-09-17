
from rest_framework import viewsets
from rest_framework.response import Response
from .models import MonetaryPenalty
from .serializers import MonetaryPenaltySerializer, FileMetadataSerializer
from fileid.models import FileMetadata

class MonetaryPenaltyViewSet(viewsets.ModelViewSet):
    queryset = MonetaryPenalty.objects.all()
    serializer_class = MonetaryPenaltySerializer

    # Specify the allowed actions (HTTP methods) for the view
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Create a MonetaryPenalty object
        monetary_penalty = serializer.save()

        # Create a JSON representation of the data
        json_data = serializer.validated_data

        # Create a new entry in FileMetadata with the JSON data
        file_metadata = FileMetadata.objects.create(
            name="MonetaryPenalty JSON Data",  # Set a name for the JSON data
            json_data=json_data,
            file_type="application/json",  # Set the appropriate content type
            description="JSON data generated from MonetaryPenalty",
        )

        # Return the JSON data and its related FileMetadata entry
        response_data = {
            "monetary_penalty_data": json_data,
            "file_metadata_id": file_metadata.file_id,
        }

        return Response(response_data, status=201)
