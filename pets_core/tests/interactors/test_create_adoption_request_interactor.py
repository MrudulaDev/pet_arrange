from mock import create_autospec
import pytest

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.create_adoption_request_interactor import CreateAdoptionRequestInteractor
from pets_core.tests.factories.storage_dtos import CreateAdoptionRequestDTOFactory
from pets_core.exceptions.custom_exceptions import InvalidPetId, PetAlreadyAdopted, AdoptionRequestAlreadyRaised, \
    UserIsNotAdopter


class TestCreateAdoptionRequestInteractor:
    @pytest.fixture()
    def mock_data(self):
        storage = create_autospec(StorageInterface)
        interactor = CreateAdoptionRequestInteractor(storage=storage)
        mock_data = (storage, interactor)
        return mock_data

    def test_with_invalid_pet_id(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        storage.validate_pet_id.side_effect = InvalidPetId(pet_id)

        # Act
        with pytest.raises(InvalidPetId) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory)

        # Assert
        assert err.value.pet_id == pet_id
        storage.validate_pet_id.assert_called_once_with(pet_id)

    def test_with_already_adopted_pet(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        storage.validate_if_pet_already_adopted.side_effect = PetAlreadyAdopted(pet_id)

        # Act
        with pytest.raises(PetAlreadyAdopted) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory)

        # Assert
        assert err.value.pet_id == pet_id
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)

    def test_with_user_that_is_not_an_adoptor(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        user_id = CreateAdoptionRequestDTOFactory.user_id
        storage.validate_if_user_is_adopter.side_effect = UserIsNotAdopter(user_id)

        # Act
        with pytest.raises(PetAlreadyAdopted) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory)

        # Assert
        assert err.value.pet_id == user_id
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)
        storage.validate_if_user_is_adopter.assert_called_once_with(user_id)

    # def test_with_user_that_is_not_an_adoptor(self, mock_data):
    #     # Arrange
    #     (storage, interactor) = mock_data
    #     pet_id = CreateAdoptionRequestDTOFactory.pet_id
    #     user_id = CreateAdoptionRequestDTOFactory.user_id
    #     storage.validate_if_user_is_adopter.side_effect = UserIsNotAdopter(user_id)
    #
    #     # Act
    #     with pytest.raises(PetAlreadyAdopted) as err:
    #         interactor.create_adoption_request(CreateAdoptionRequestDTOFactory)
    #
    #     # Assert
    #     assert err.value.pet_id == user_id
    #     storage.validate_pet_id.assert_called_once_with(pet_id)
    #     storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)
    #     storage.validate_if_user_is_adopter.assert_called_once_with(user_id)


    # def test_with_valid_data(self, mock_data):
    #     # Arrange
    #     mock = mock_data
    #     storage_pet_details = PetDetailsDTOFactory()
    #     mock["storage"].get_pet.return_value = storage_pet_details
    #     pet_id = storage_pet_details.pet_id
    #     user_id = "4e00b2e7-0a0d-4f53-8dcf-34530d46d06a"
    #
    #     # Act
    #     pet_details_dto = mock["interactor"].get_pet("4e00b2e7-0a0d-4f53-8dcf-34530d46d06a", pet_id)
    #
    #     # Assert
    #     assert storage_pet_details == pet_details_dto
    #     mock["storage"].validate_pet_id.assert_called_once_with(pet_id)
    #     mock["storage"].validate_user_access_to_pet_shelter.assert_called_with(pet_id=pet_id, user_id=user_id)
    #     mock["storage"].get_pet.assert_called_once_with(pet_id)
