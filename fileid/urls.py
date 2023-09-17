from django.urls import path
from .views import FileMetadataViewSet

# Define your URL patterns
urlpatterns = [
    path('file-metadata/<uuid:file_id>/', FileMetadataViewSet.as_view({'get': 'retrieve'}), name='file-metadata-detail'),
]
