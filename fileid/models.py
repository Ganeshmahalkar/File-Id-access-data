import uuid
from django.db import models

class FileMetadata(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    json_data = models.JSONField()  # Import JSONField from django.db.models
    file_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'FILE'
        
    # def save(self, *args, **kwargs):
    #     # Convert the UUID to the hyphenated format before saving
    #     self.file_id = str(self.file_id)
    #     super().save(*args, **kwargs)


