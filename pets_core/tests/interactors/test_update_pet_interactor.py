from mock import create_autospec
from mock.mock import Mock, patch
import pytest

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.update_pet_interactor import UpdatePetInteractor
from pets_core.interactors.create_pet_interactor import CreatePetInteractor
from pets_core.tests.factories.storage_dtos import UpdatePetDetailsDTOFactory, PetDetailsDTOFactory
from pets_core.exceptions.custom_exceptions import PetNotFoundInShelter, InvalidAge, NameAlreadyExists


class TestUpdatePetInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = UpdatePetInteractor(storage=storage)
        mock_data = {"storage": storage, "interactor": interactor}
        return mock_data

    def test_with_non_existing_pet_id(self, mock_data):
        # Arrange
        mock = mock_data
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
        update_pet_details = UpdatePetDetailsDTOFactory()
        pet_id = update_pet_details.pet_id
        mock["storage"].validate_if_pet_exists_in_user_shelter.side_effect = PetNotFoundInShelter(pet_id)

        # Act
        with pytest.raises(PetNotFoundInShelter) as err:
            mock["interactor"].update_pet(user_id=user_id, pet_details_dto=update_pet_details)

        # Assert
        assert err.value.pet_id == pet_id
        mock["storage"].validate_if_pet_exists_in_user_shelter.assert_called_once_with(pet_id=pet_id, user_id=user_id)

    def test_with_existing_pet_name(self, mock_data):
        # Arrange
        mock = mock_data
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
        update_pet_details = UpdatePetDetailsDTOFactory()
        pet_id = update_pet_details.pet_id
        pet_name = update_pet_details.name
        mock["storage"].validate_if_pet_name_already_exists.side_effect = NameAlreadyExists(pet_name)

        # Act
        with pytest.raises(NameAlreadyExists) as err:
            mock["interactor"].update_pet(user_id=user_id, pet_details_dto=update_pet_details)

        # Assert
        assert err.value.name == pet_name
        mock["storage"].validate_if_pet_exists_in_user_shelter.assert_called_once_with(pet_id=pet_id, user_id=user_id)
        mock["storage"].validate_if_pet_name_already_exists.assert_called_once_with(name=pet_name)

    @patch.object(CreatePetInteractor, 'validate_age')
    def test_with_invalid_age(self, validate_age, mock_data):
        # Arrange
        mock = mock_data
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
        update_pet_details = UpdatePetDetailsDTOFactory()
        pet_id = update_pet_details.pet_id
        pet_name = update_pet_details.name
        age = update_pet_details.age
        validate_age.side_effect = InvalidAge(age)

        # Act
        with pytest.raises(InvalidAge) as err:
            mock["interactor"].update_pet(user_id=user_id, pet_details_dto=update_pet_details)

        # Assert
        assert err.value.age == age
        mock["storage"].validate_if_pet_exists_in_user_shelter.assert_called_once_with(pet_id=pet_id, user_id=user_id)
        mock["storage"].validate_if_pet_name_already_exists.assert_called_once_with(name=pet_name)
        validate_age.assert_called_once_with(age=age)

    @patch.object(CreatePetInteractor, 'validate_age')
    def test_with_valid_data(self, validate_age, mock_data):
        # Arrange
        mock = mock_data
        user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
        update_pet_details = UpdatePetDetailsDTOFactory()
        pet_details_dto = PetDetailsDTOFactory()
        pet_id = update_pet_details.pet_id
        pet_name = update_pet_details.name
        age = update_pet_details.age
        mock["storage"].update_pet.return_value = pet_details_dto
        # Act
        update_pet_return_value = mock["interactor"].update_pet(user_id=user_id, pet_details_dto=update_pet_details)

        # Assert
        assert pet_details_dto == update_pet_return_value
        mock["storage"].validate_if_pet_exists_in_user_shelter.assert_called_once_with(pet_id=pet_id, user_id=user_id)
        mock["storage"].validate_if_pet_name_already_exists.assert_called_once_with(name=pet_name)
        validate_age.assert_called_once_with(age=age)
        mock["storage"].update_pet.assert_called_once_with(pet_details_dto=update_pet_details)
