import pytest

from pets_core.models.pet import Pet
from pets_core.storages.storage_implementation import StorageImplementation


class TestGetPet:
    @pytest.mark.django_db
    def test_with_valid_pet_id_gives_pet_details_dto(self, get_pet):
        # Arrange
        pet_id = "1"
        sql_storage = StorageImplementation()
        pet_object = Pet.objects.get(pet_id=pet_id)

        # Act
        pet_details = sql_storage.get_pet(pet_id=pet_id)

        # Assert
        assert pet_details.pet_id == pet_object.pet_id
        assert pet_details.name == pet_object.name
        assert pet_details.pet_category == pet_object.pet_category
        assert pet_details.gender == pet_object.gender
        assert pet_details.size == pet_object.size
        assert pet_details.age == pet_object.age
        assert pet_details.status == pet_object.status
