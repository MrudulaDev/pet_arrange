from mock import create_autospec
import pytest
from mock.mock import patch
from pets_core.interactors.get_adoption_requests_list_interactor import GetAdoptionRequestsListInteractor
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestsListDTOFactory, AdoptionRequestDTOFactory
from pets_core.exceptions.custom_exceptions import ShelterNotFound, WrongShelterId


class TestGetAdoptionRequestInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = GetAdoptionRequestsListInteractor(storage=storage)
        mock_data = (storage, interactor)
        return mock_data

    def test_with_invalid_shelter_id(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_requests_lis_dto_factory = GetAdoptionRequestsListDTOFactory()
        shelter_id = get_adoption_requests_lis_dto_factory.shelter_id
        storage.validate_if_shelter_exists.side_effect = ShelterNotFound(shelter_id)

        # Act
        with pytest.raises(ShelterNotFound) as err:
            interactor.get_adoption_requests_list(get_adoption_requests_lis_dto_factory)

        # Assert
        assert err.value.shelter_id == shelter_id
        storage.validate_if_shelter_exists.assert_called_once_with(shelter_id=shelter_id)

    def test_with_wrong_shelter_id(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_requests_list_dto_factory = GetAdoptionRequestsListDTOFactory()
        shelter_id = get_adoption_requests_list_dto_factory.shelter_id
        user_id = get_adoption_requests_list_dto_factory.user_id
        storage.validate_if_user_is_shelter.side_effect = WrongShelterId(shelter_id)

        # Act
        with pytest.raises(WrongShelterId) as err:
            interactor.get_adoption_requests_list(get_adoption_requests_list_dto_factory)

        # Assert
        assert err.value.shelter_id == shelter_id
        storage.validate_if_shelter_exists.assert_called_once_with(shelter_id=shelter_id)
        storage.validate_if_user_is_shelter.assert_called_once_with(shelter_id=shelter_id, user_id=user_id)

    def test_get_adoption_requests_list(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        get_adoption_requests_list_dto_factory = GetAdoptionRequestsListDTOFactory()
        shelter_id = get_adoption_requests_list_dto_factory.shelter_id
        user_id = get_adoption_requests_list_dto_factory.user_id
        adoption_requests_list_dto_factory = [AdoptionRequestDTOFactory]
        storage.get_adoption_requests_list.return_value = adoption_requests_list_dto_factory

        # Act
        adoption_request_dtos_list = interactor.get_adoption_requests_list(get_adoption_requests_list_dto_factory)

        # Assert
        assert adoption_request_dtos_list == adoption_requests_list_dto_factory
        storage.validate_if_shelter_exists.assert_called_once_with(shelter_id=shelter_id)
        storage.validate_if_user_is_shelter.assert_called_once_with(shelter_id=shelter_id, user_id=user_id)
        storage.get_adoption_requests_list.assert_called_once_with(get_adoption_requests_list_dto=get_adoption_requests_list_dto_factory)