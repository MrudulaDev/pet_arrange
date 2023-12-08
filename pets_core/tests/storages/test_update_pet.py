import pytest

from pets_core.models.pet import Pet
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import UpdatePetDetailsDTOFactory


class TestUpdatePet:
    @pytest.mark.django_db
    def test_with_valid_data(self,create_pet):
        # Arrange
        storage = StorageImplementation()
        pet_details_dto = UpdatePetDetailsDTOFactory()
        # Act
        pet_dto= storage.update_pet(pet_details_dto)
        # Assert
        assert pet_details_dto.pet_id == pet_dto.pet_id
        assert pet_details_dto.name == pet_dto.name
        assert pet_details_dto.pet_category == pet_dto.pet_category
        assert pet_details_dto.gender == pet_dto.gender
        assert pet_details_dto.pet_size == pet_dto.size
        assert pet_details_dto.age == pet_dto.age
