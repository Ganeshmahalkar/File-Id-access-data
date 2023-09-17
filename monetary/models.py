from django.db import models
import uuid

class MonetaryPenalty(models.Model):
    monetary_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity_id = models.CharField(max_length=255, blank=True, null=True)
    premiseId = models.CharField(max_length=255, blank=True, null=True)
    startDate = models.CharField(max_length=255, blank=True, null=True)
    endDate = models.CharField(max_length=255, blank=True, null=True)
    penaltyAuthority = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'MonetaryPenalty'
        
    # def save(self, *args, **kwargs):
    #     # Convert the UUID to the hyphenated format before saving
    #     self.monetary_id = str(self.monetary_id)
    #     super().save(*args, **kwargs)
