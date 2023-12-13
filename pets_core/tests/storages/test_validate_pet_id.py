import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import InvalidPetId


class TestValidatePetId:
    @pytest.mark.django_db
    def test_with_valid_pet_id(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        pet_id = 1

        # Act
        storage.validate_pet_id(pet_id=pet_id)


    @pytest.mark.django_db
    def test_with_invalid_pet_id(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        pet_id = 10

        # Act
        with pytest.raises(InvalidPetId) as err:
            storage.validate_pet_id(pet_id=pet_id)

        # Assert
        assert err.value.pet_id == pet_id
