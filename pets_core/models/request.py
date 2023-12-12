from django.db import models
from pets_core.constants.enums import RequestStatus
from pets_core.models.pet import Pet
from pets_core.models.adopter import Adopter


class Request(models.Model):
    RequestStatus_Choice = (
        (RequestStatus.OPEN.value, RequestStatus.OPEN.value),
        (RequestStatus.APPROVED.value, RequestStatus.APPROVED.value),
        (RequestStatus.CLOSED.value, RequestStatus.CLOSED.value)
    )
    request_id = models.IntegerField(primary_key=True)
    request_status = models.CharField(max_length=20, choices=RequestStatus_Choice, default=RequestStatus.OPEN.value)
    requested_by = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='requests')
    requested_pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='requests')
    requested_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    status_change_timestamp = models.DateTimeField(null=True, blank=True)  # Updated whenever status changes


def __str__(self):
    return self.request_id
