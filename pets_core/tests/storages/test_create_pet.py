import pytest
from pets_core.models.pet import Pet
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import PetDetailsDTOFactory


class TestCreatePet:
    @pytest.mark.django_db
    def test_with_valid_data(self, create_shelters):
        # Arrange
        storage = StorageImplementation()
        pet_details_dto = PetDetailsDTOFactory()
        # Act
        created_pet = storage.create_pet(pet_details_dto)
        # Assert
        assert created_pet.pet_id == pet_details_dto.pet_id
        assert created_pet.name == pet_details_dto.name
        assert created_pet.pet_category == pet_details_dto.pet_category
        assert created_pet.gender == pet_details_dto.gender
        assert created_pet.pet_size == pet_details_dto.pet_size
        assert created_pet.shelter_id == pet_details_dto.shelter_id
        assert created_pet.age == pet_details_dto.age
        assert created_pet.status == pet_details_dto.status
