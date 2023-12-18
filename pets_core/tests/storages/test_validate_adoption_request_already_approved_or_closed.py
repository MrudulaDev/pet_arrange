import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestAlreadyApproved, AdoptionRequestClosed
from pets_core.models.adopter import Adopter
from pets_core.models.request import Request
from pets_core.constants.enums import RequestStatus


class TestValidateAdoptionRequestAlreadyApprovedOrClosed:

    @pytest.fixture(autouse=True)
    def setup(self, db, load_adoption_requests):
        # This fixture is called before each test method
        pass

    @pytest.mark.django_db
    def test_with_approved_request(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 1
        Request.objects.filter(request_id=request_id).update(request_status=RequestStatus.APPROVED.value)

        # Act
        with pytest.raises(AdoptionRequestAlreadyApproved) as err:
            storage.validate_adoption_request_already_approved_or_closed(request_id=request_id)

        # Assert
        assert err.value.request_id == request_id

    @pytest.mark.django_db
    def test_with_closed_request(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 2
        ids_list = Request.objects.values_list('request_id', flat=True)
        Request.objects.filter(request_id=request_id).update(request_status=RequestStatus.CLOSED.value)
        # Act
        with pytest.raises(AdoptionRequestClosed) as err:
            storage.validate_adoption_request_already_approved_or_closed(request_id=request_id)

        # Assert
        assert err.value.request_id == request_id

    @pytest.mark.django_db
    def test_with_open_request(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 4

        # Act
        storage.validate_adoption_request_already_approved_or_closed(request_id=request_id)
