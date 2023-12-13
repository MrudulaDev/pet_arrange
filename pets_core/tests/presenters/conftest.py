import pytest
from datetime import datetime
from pets_core.models.pet import Pet
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus, RequestStatus
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, AdoptionRequestDTO


@pytest.fixture()
def pet_details_dto():
    return PetDetailsDTO(
        pet_id=1,
        name="husky",
        age=1,
        pet_category=PetCategory.DOG.value,
        pet_size=PetSize.SMALL.value,
        gender=PetGender.FEMALE.value,
        status=PetStatus.AVAILABLE.value,
        shelter_id=1
    )


@pytest.fixture()
def adoption_request_dto():
    return AdoptionRequestDTO(
        request_id=1,
        request_status=RequestStatus.OPEN.value,
        pet_id=1,
        adopter_id=1,
        requested_at=datetime.now()
    )
