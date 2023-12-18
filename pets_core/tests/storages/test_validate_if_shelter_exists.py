import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import ShelterNotFound


class TestValidateIfShelterExists:
    @pytest.mark.django_db
    def test_with_valid_shelter_id(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        shelter_id = 1

        # Act
        storage.validate_if_shelter_exists(shelter_id=shelter_id)

    @pytest.mark.django_db
    def test_with_invalid_shelter_id(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        shelter_id = 10

        # Act
        with pytest.raises(ShelterNotFound) as err:
            storage.validate_if_shelter_exists(shelter_id=shelter_id)

        # Assert
        assert err.value.shelter_id == shelter_id
