import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import UserIsNotAdopter


class TestValidateUserIsAdopter:
    @pytest.mark.django_db
    def test_when_user_is_adopter(self, create_shelters_and_pets, load_adopters):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'

        # Act
        storage.validate_if_user_is_adopter(user_id=user_id)

    @pytest.mark.django_db
    def test_when_user_is_not_adopter(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'

        # Act
        with pytest.raises(UserIsNotAdopter) as err:
            storage.validate_if_user_is_adopter(user_id=user_id)

        # Assert
        assert err.value.user_id == user_id
