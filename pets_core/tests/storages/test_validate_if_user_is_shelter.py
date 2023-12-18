import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import WrongShelterId
from pets_core.models.shelter import Shelter


class TestValidateIfShelterExists:
    @pytest.mark.django_db
    def test_with_valid_shelter_user(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        shelter_id = 1
        user_id = Shelter.objects.filter(shelter_id=shelter_id).values_list('user_id', flat=True).first()

        # Act
        storage.validate_if_user_is_shelter(shelter_id=shelter_id, user_id=user_id)

    @pytest.mark.django_db
    def test_with_invalid_shelter_user(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        shelter_id = 1
        user_id = ""

        # Act
        with pytest.raises(WrongShelterId) as err:
            storage.validate_if_user_is_shelter(shelter_id=shelter_id, user_id=user_id)

        # Assert
        assert err.value.shelter_id == shelter_id
