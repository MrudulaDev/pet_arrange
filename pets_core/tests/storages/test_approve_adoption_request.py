import pytest
from freezegun import freeze_time
from datetime import datetime
from pets_core.models.request import Request
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound
from pets_core.tests.factories.storage_dtos import ApproveAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.constants.enums import RequestStatus
from pets_core.models.adopter import Adopter


class TestApproveAdoptionRequest:
    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_valid_data(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 1
        Request.objects.update(requested_at=str(datetime.now()))
        adopter_id = Adopter.objects.filter(user_id='user2').values_list('id', flat=True).first()
        request_dto_factory = AdoptionRequestDTOFactory(adopter_id=adopter_id, requested_at=str(datetime.now()),
                                                        request_status=RequestStatus.APPROVED.value)
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()

        # Act
        fetched_request_dto = storage.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert fetched_request_dto.request_id == request_dto_factory.request_id
        assert fetched_request_dto.request_status == request_dto_factory.request_status
        assert fetched_request_dto.pet_id == request_dto_factory.pet_id
        assert fetched_request_dto.adopter_id == request_dto_factory.adopter_id
        assert fetched_request_dto.requested_at == request_dto_factory.requested_at
