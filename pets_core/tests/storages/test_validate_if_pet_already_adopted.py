import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import PetAlreadyAdopted
from pets_core.constants.enums import PetStatus
from pets_core.models.pet import Pet


class TestValidatePetAlreadyAdopted:
    @pytest.mark.django_db
    def test_with_pet_status_adopted(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        pet_id = 1
        pet = Pet.objects.get(pet_id=pet_id)
        pet.status = PetStatus.ADOPTED.value
        pet.save()

        # Act
        with pytest.raises(PetAlreadyAdopted) as err:
            storage.validate_if_pet_already_adopted(pet_id=pet_id)

        # Assert
        assert err.value.pet_id == pet_id

    @pytest.mark.django_db
    def test_with_pet_status_available(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        pet_id = 1
        pet = Pet.objects.get(pet_id=pet_id)
        pet.status = PetStatus.AVAILABLE.value
        pet.save()

        # Act
        storage.validate_if_pet_already_adopted(pet_id=pet_id)
