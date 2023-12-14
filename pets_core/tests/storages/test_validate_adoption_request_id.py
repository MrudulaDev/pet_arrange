import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound


class TestValidateAdoptionRequestId:
    @pytest.mark.django_db
    def test_with_valid_request_id(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 1

        # Act
        storage.validate_adoption_request_id(request_id=request_id)

    @pytest.mark.django_db
    def test_with_invalid_request_id(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        request_id = 10

        # Act
        with pytest.raises(AdoptionRequestNotFound) as err:
            storage.validate_adoption_request_id(request_id=request_id)

        # Assert
        assert err.value.request_id == request_id
