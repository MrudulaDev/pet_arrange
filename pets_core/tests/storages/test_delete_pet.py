import pytest
from pets_core.models.pet import Pet
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import PetDetailsDTOFactory


class TestCreatePet:
    @pytest.mark.django_db
    def test_with_valid_data(self, create_pet):
        # Arrange
        storage = StorageImplementation()
        pet = create_pet

        # Act
        storage.delete_pet(pet_id=pet.pet_id)

        # Assert
        assert not Pet.objects.filter(pet_id=pet.pet_id).exists()