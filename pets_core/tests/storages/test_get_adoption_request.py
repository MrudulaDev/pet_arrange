import pytest
from freezegun import freeze_time
from datetime import datetime
from pets_core.models.request import Request
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.constants.enums import RequestStatus


class TestValidateGetAdoptionRequest:
    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_valid_data(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        adopter_id = 2
        Request.objects.update(requested_at=str(datetime.now()))
        request_dto_factory = AdoptionRequestDTOFactory(adopter_id=adopter_id, requested_at=str(datetime.now()))
        get_adoption_request_dto = GetAdoptionRequestDTOFactory()

        # Act
        fetched_request_dto = storage.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert fetched_request_dto.request_id == request_dto_factory.request_id
        assert fetched_request_dto.request_status == request_dto_factory.request_status
        assert fetched_request_dto.pet_id == request_dto_factory.pet_id
        assert fetched_request_dto.adopter_id == request_dto_factory.adopter_id
        assert fetched_request_dto.requested_at == request_dto_factory.requested_at
