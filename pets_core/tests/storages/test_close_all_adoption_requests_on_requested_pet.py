import pytest
from freezegun import freeze_time
from datetime import datetime
from pets_core.models.request import Request
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound
from pets_core.tests.factories.storage_dtos import ApproveAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.constants.enums import RequestStatus
from pets_core.models.adopter import Adopter


class TestCloseAllRequests:
    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_valid_data(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 1

        # Act
        storage.close_all_adoption_requests_on_requested_pet(request_id=request_id)

        # Assert
        requests_list = Request.objects.exclude(request_id=request_id)
        for request in requests_list:
            assert request.request_status == RequestStatus.CLOSED.value, (
                f"Instance {request.request_id} does not have the expected value."
            )
            assert str(request.status_change_timestamp) == str(datetime.now()), (
                f"Instance {request.request_id} does not have the expected value."
            )