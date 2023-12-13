import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.models.adopter import Adopter


class TestGetAdopterId:
    @pytest.mark.django_db
    def test_with_valid_data(self, create_shelters_and_pets, load_adopters):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'
        adopter_id = Adopter.objects.get(user_id=user_id).id

        # Act
        adopter_id_returned = storage.get_adopter_id(user_id=user_id)

        # Assert
        assert adopter_id_returned == adopter_id

    @pytest.mark.django_db
    def test_with_invalid_data(self, create_shelters_and_pets, load_adopters):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'
        adopter_id = Adopter.objects.get(user_id='user2').id

        # Act
        adopter_id_returned = storage.get_adopter_id(user_id=user_id)

        # Assert
        assert adopter_id_returned != adopter_id
