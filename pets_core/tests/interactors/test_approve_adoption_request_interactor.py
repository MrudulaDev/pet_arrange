from mock import create_autospec
import pytest
from mock.mock import patch
from pets_core.interactors.adoption_request_access_interactor import AdoptionRequestAccess
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.approve_adoption_request_interactor import ApproveAdoptionRequestInteractor
from pets_core.tests.factories.storage_dtos import ApproveAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound, AdoptionRequestAccessDenied, \
    AdoptionRequestAlreadyApproved, AdoptionRequestClosed


class TestApproveAdoptionRequestInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = ApproveAdoptionRequestInteractor(storage=storage)
        mock_data = (storage, interactor)
        return mock_data

    def test_with_invalid_request_id(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        storage.validate_adoption_request_id.side_effect = AdoptionRequestNotFound(request_id=request_id)

        # Act
        with pytest.raises(AdoptionRequestNotFound) as err:
            interactor.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert err.value.request_id == request_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_invalid_user(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        user_id = approve_adoption_request_dto.user_id
        validate_adoption_request_access.side_effect = AdoptionRequestAccessDenied(user_id)

        # Act
        with pytest.raises(AdoptionRequestAccessDenied) as err:
            interactor.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert err.value.user_id == user_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_already_approved_request(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        user_id = approve_adoption_request_dto.user_id
        storage.validate_adoption_request_already_approved_or_closed.side_effect = AdoptionRequestAlreadyApproved(
            request_id)

        # Act
        with pytest.raises(AdoptionRequestAlreadyApproved) as err:
            interactor.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert err.value.request_id == request_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)
        storage.validate_adoption_request_already_approved_or_closed.assert_called_once_with(request_id=request_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_closed_request(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        user_id = approve_adoption_request_dto.user_id
        storage.validate_adoption_request_already_approved_or_closed.side_effect = AdoptionRequestClosed(
            request_id)

        # Act
        with pytest.raises(AdoptionRequestClosed) as err:
            interactor.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert err.value.request_id == request_id
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)
        storage.validate_adoption_request_already_approved_or_closed.assert_called_once_with(request_id=request_id)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_with_valid_data(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        user_id = approve_adoption_request_dto.user_id
        storage.approve_adoption_request.return_value = AdoptionRequestDTOFactory()

        # Act
        adoption_request_dto = interactor.approve_adoption_request(
            approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        assert adoption_request_dto == AdoptionRequestDTOFactory()
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)
        storage.validate_adoption_request_already_approved_or_closed.assert_called_once_with(request_id=request_id)
        storage.approve_adoption_request.assert_called_once_with(
            approve_adoption_request_dto=approve_adoption_request_dto)

    @patch.object(AdoptionRequestAccess, 'validate_adoption_request_access')
    def test_close_all_other_adoption_requests_on_requested_pet(self, validate_adoption_request_access, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        approve_adoption_request_dto = ApproveAdoptionRequestDTOFactory()
        request_id = approve_adoption_request_dto.request_id
        user_id = approve_adoption_request_dto.user_id

        # Act
        interactor.approve_adoption_request(approve_adoption_request_dto=approve_adoption_request_dto)

        # Assert
        storage.validate_adoption_request_id.assert_called_once_with(request_id=request_id)
        validate_adoption_request_access.assert_called_once_with(request_id=request_id, user_id=user_id)
        storage.validate_adoption_request_already_approved_or_closed.assert_called_once_with(request_id=request_id)
        storage.approve_adoption_request.assert_called_once_with(
            approve_adoption_request_dto=approve_adoption_request_dto)
        storage.close_all_other_adoption_requests_on_requested_pet.assert_called_once_with(request_id=request_id)
