from pets_core.models.request import Request
from pets_core.exceptions.custom_exceptions import AdoptionRequestAccessDenied


class AdoptionRequestAccess:

    def validate_adoption_request_access(self, request_id: int, user_id: str):
        request = Request.objects.get(request_id=request_id)
        pet = request.requested_pet
        adopter = request.requested_by
        requested_pet_shelter_user_id = pet.shelter.user_id
        requested_pet_adopter_user_id = adopter.user_id
        if user_id not in [requested_pet_shelter_user_id, requested_pet_adopter_user_id]:
            raise AdoptionRequestAccessDenied(user_id=user_id)
