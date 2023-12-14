from mock import create_autospec
import pytest

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.get_adoption_request_interactor import GetAdoptionRequestInteractor
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestDTOFactory
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound, AdoptionRequestAccessDenied


class TestGetAdoptionRequestInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = GetAdoptionRequestInteractor(storage=storage)
        mock_data = (storage, interactor)
        return mock_data

    def test_with_invalid_request_id(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_request_dto = GetAdoptionRequestDTOFactory(request_id=3)
        request_id = 3
        storage.validate_adoption_request_id.side_effect = AdoptionRequestNotFound(request_id)

        # Act
        with pytest.raises(AdoptionRequestNotFound) as err:
            interactor.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert err.value.request_id == request_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id)

    def test_with_invalid_shelter(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_request_dto = GetAdoptionRequestDTOFactory()
        request_id = get_adoption_request_dto.request_id
        user_id = get_adoption_request_dto.user_id
        interactor.validate_adoption_request_access.side_effect = AdoptionRequestAccessDenied(user_id)

        # Act
        with pytest.raises(AdoptionRequestAccessDenied) as err:
            interactor.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert err.value.user_id == user_id
        interactor.assert_called_once_with(request_id, user_id)
