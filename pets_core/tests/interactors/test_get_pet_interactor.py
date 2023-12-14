from mock import create_autospec
from mock.mock import Mock
import pytest

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.get_pet_interactor import GetPetInteractor
from pets_core.tests.factories.storage_dtos import PetDetailsDTOFactory
from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId


class TestGetPetInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = GetPetInteractor(storage=storage)
        mock_data = {"storage": storage, "interactor": interactor}
        return mock_data

    def test_with_invalid_pet_id(self, mock_data):
        # Arrange
        mock = mock_data
        # todo: use kwargs in instantiation
        mock["storage"].validate_pet_id.side_effect = InvalidPetId(2)
        pet_id = 2
        # Act
        with pytest.raises(InvalidPetId) as err:
            mock["interactor"].get_pet(pet_id=2, user_id="")

        # Assert
        assert err.value.pet_id == 2
        mock["storage"].validate_pet_id.assert_called_once_with(pet_id)

    def test_with_wrong_shelter(self, mock_data):
        # Arrange
        mock = mock_data
        mock["storage"].validate_user_access_to_pet_shelter.side_effect = WrongShelterId(1)
        pet_id = 2
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
        # Act
        with pytest.raises(WrongShelterId) as err:
            mock["interactor"].get_pet("4e00b2e7-0a0d-4f53-8dcf-34530d46d06a", 2)

        # Assert
        assert err.value.shelter_id == 1
        mock["storage"].validate_pet_id.assert_called_once_with(pet_id)
        mock["storage"].validate_user_access_to_pet_shelter.assert_called_with(pet_id=pet_id, user_id=user_id)

    def test_with_valid_data(self, mock_data):
        # Arrange
        mock = mock_data
        storage_pet_details = PetDetailsDTOFactory()
        mock["storage"].get_pet.return_value = storage_pet_details
        pet_id = storage_pet_details.pet_id
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"

        # Act
        pet_details_dto = mock["interactor"].get_pet("4e00b2e7-0a0d-4f53-8dcf-34530d46d06a", pet_id)

        # Assert
        assert storage_pet_details == pet_details_dto
        mock["storage"].validate_pet_id.assert_called_once_with(pet_id)
        mock["storage"].validate_user_access_to_pet_shelter.assert_called_with(pet_id=pet_id, user_id=user_id)
        mock["storage"].get_pet.assert_called_once_with(pet_id)
