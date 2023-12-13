from mock import create_autospec
import pytest

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.create_adoption_request_interactor import CreateAdoptionRequestInteractor
from pets_core.tests.factories.storage_dtos import CreateAdoptionRequestDTOFactory, AdoptionRequestDTOFactory
from pets_core.exceptions.custom_exceptions import InvalidPetId, PetAlreadyAdopted, AdoptionRequestAlreadyRaised, \
    UserIsNotAdopter

class TestCreateAdoptionRequestInteractor:
    @pytest.fixture()
    def mock_data(self):
        # todo: this approach is also valid, but we use a different way in our project,
        #  we shall discuss later on this
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
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory())

        # Assert
        assert err.value.pet_id == pet_id
        # todo: assert with kwargs, same review point for all remaining tests
        storage.validate_pet_id.assert_called_once_with(pet_id)

    def test_with_already_adopted_pet(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        storage.validate_if_pet_already_adopted.side_effect = PetAlreadyAdopted(pet_id)

        # Act
        with pytest.raises(PetAlreadyAdopted) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory())

        # Assert
        assert err.value.pet_id == pet_id
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)

    def test_with_user_that_is_not_an_adopter(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        user_id = CreateAdoptionRequestDTOFactory.user_id
        storage.validate_if_user_is_adopter.side_effect = UserIsNotAdopter(user_id)

        # Act
        with pytest.raises(UserIsNotAdopter) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory())

        # Assert
        assert err.value.user_id == user_id
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)
        storage.validate_if_user_is_adopter.assert_called_once_with(user_id)

    def test_with_duplicate_request(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        user_id = CreateAdoptionRequestDTOFactory.user_id
        adopter_id = 1
        request_id = 1
        storage.validate_if_request_already_raised.side_effect = AdoptionRequestAlreadyRaised(request_id)
        storage.get_adopter_id.return_value = adopter_id

        # Act
        with pytest.raises(AdoptionRequestAlreadyRaised) as err:
            interactor.create_adoption_request(CreateAdoptionRequestDTOFactory())

        # Assert
        assert err.value.request_id == request_id
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)
        storage.validate_if_user_is_adopter.assert_called_once_with(user_id)
        storage.get_adopter_id.assert_called_once_with(user_id)
        storage.validate_if_request_already_raised.assert_called_once_with(pet_id, adopter_id)

    def test_with_valid_data(self, mock_data):
        # Arrange
        (storage, interactor) = mock_data
        pet_id = CreateAdoptionRequestDTOFactory.pet_id
        user_id = CreateAdoptionRequestDTOFactory.user_id
        adopter_id = 1
        request_id = 1
        storage.get_adopter_id.return_value = adopter_id
        create_request_dto_factory = CreateAdoptionRequestDTOFactory()
        request_dto_factory = AdoptionRequestDTOFactory()
        storage.create_adoption_request.return_value = request_dto_factory

        # Act
        created_request_dto = interactor.create_adoption_request(create_request_dto_factory)

        # Assert
        assert request_dto_factory == created_request_dto
        storage.validate_pet_id.assert_called_once_with(pet_id)
        storage.validate_if_pet_already_adopted.assert_called_once_with(pet_id)
        storage.validate_if_user_is_adopter.assert_called_once_with(user_id)
        storage.get_adopter_id.assert_called_once_with(user_id)
        storage.validate_if_request_already_raised.assert_called_once_with(pet_id, adopter_id)
        storage.create_adoption_request.assert_called_once_with(create_request_dto_factory, adopter_id)

