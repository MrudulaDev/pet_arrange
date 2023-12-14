import pytest
from datetime import datetime
from freezegun import freeze_time
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import CreateAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.tests.factories.models import AdopterFactory


class TestCreateAdoptionRequest:
    @pytest.mark.django_db
    @freeze_time(str(datetime.now()))
    def test_create_request(self, create_shelters_and_pets):
        # Arrange
        storage = StorageImplementation()
        create_request_dto_factory = CreateAdoptionRequestDTOFactory()
        adopter = AdopterFactory(user_id="user1")
        adopter_id = adopter.id
        # todo: this doesn't work as expected, this will generate current datetime always
        now = datetime.now()
        adoption_request_dto = AdoptionRequestDTOFactory(adopter_id=adopter_id, requested_at=now)

        # Act
        created_request_dto = storage.create_adoption_request(create_request_dto_factory, adopter_id)

        # Assert
        assert created_request_dto.request_id == 1
        assert created_request_dto.request_status == adoption_request_dto.request_status
        assert created_request_dto.pet_id == adoption_request_dto.pet_id
        assert created_request_dto.adopter_id == adoption_request_dto.adopter_id
        assert created_request_dto.requested_at == str(adoption_request_dto.requested_at)
