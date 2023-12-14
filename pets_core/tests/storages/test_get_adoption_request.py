import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.constants.enums import RequestStatus


class TestValidateGetAdoptionRequest:
    @pytest.mark.django_db
    def test_with_valid_data(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        get_adoption_request_dto = GetAdoptionRequestDTOFactory()
        request_dto = AdoptionRequestDTOFactory(request_id =1, request_status = RequestStatus.OPEN.value, pet_id =1, adopter_id =1, )

        # Act
        fetched_request_dto = storage.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert

