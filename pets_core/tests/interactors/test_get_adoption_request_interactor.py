from mock import create_autospec
import pytest
from mock.mock import patch
from pets_core.interactors.adoption_request_access_interactor import AdoptionRequestAccess
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.get_adoption_request_interactor import GetAdoptionRequestInteractor
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
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
        request_id = 3
        get_adoption_request_dto = GetAdoptionRequestDTOFactory(request_id=request_id)
        storage.validate_adoption_request_id.side_effect = AdoptionRequestNotFound(request_id)

        # Act
        with pytest.raises(AdoptionRequestNotFound) as err:
            interactor.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert err.value.request_id == request_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_invalid_user(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_request_dto = GetAdoptionRequestDTOFactory()
        request_id = get_adoption_request_dto.request_id
        user_id = get_adoption_request_dto.user_id
        validate_adoption_request_access.side_effect = AdoptionRequestAccessDenied(user_id)

        # Act
        with pytest.raises(AdoptionRequestAccessDenied) as err:
            interactor.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert err.value.user_id == user_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_valid_data(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_request_dto = GetAdoptionRequestDTOFactory()
        request_id = get_adoption_request_dto.request_id
        user_id = get_adoption_request_dto.user_id
        adoption_request_dto_factory = AdoptionRequestDTOFactory()
        storage.get_adoption_request.return_value = adoption_request_dto_factory

        # Act
        created_adoption_request = interactor.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)

        # Assert
        assert created_adoption_request == adoption_request_dto_factory
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)
        storage.get_adoption_request.assert_called_once_with(get_adoption_request_dto=get_adoption_request_dto)
