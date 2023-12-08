import pytest
from pets_core.models.pet import Pet
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


@pytest.fixture()
def pet_details_dto():
    return PetDetailsDTO(
        pet_id=1,
        name="husky",
        age=1,
        pet_category=PetCategory.DOG.value,
        size=PetSize.SMALL.value,
        gender=PetGender.FEMALE.value,
        status=PetStatus.AVAILABLE.value,
        shelter_id=1
    )
