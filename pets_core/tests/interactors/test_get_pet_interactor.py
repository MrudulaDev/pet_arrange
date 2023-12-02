from mock import create_autospec
from mock.mock import Mock

from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.get_pet_interactor import GetPetInteractor


class TestGetPetInteractor:

    def test_get_pet_with_valid_pet_id_returns_pet_details_dto(self):
        #Arrange
        storage = create_autospec(StorageInterface)
        interactor = GetPetInteractor(storage=storage)
        storage_get_pet_return_value = Mock()
        storage.get_pet.return_value = storage_get_pet_return_value
        #Act
        pet_details_dto = interactor.get_pet(pet_id=1, user_id="")
        #Assert
        assert pet_details_dto == storage.get_pet.return_value

    def test_get_pet_with_invalid_pet_id_raises_InvalidPetId_error(self):

        storage = create_autospec(StorageInterface)
        interactor = GetPetInteractor(storage=storage)
        storage_get_pet_return_value = Mock()
        storage.get_pet.return_value = storage_get_pet_return_value

        pet_details_dto = interactor.get_pet(pet_id=1, user_id="")

        assert pet_details_dto == storage.get_pet.return_value
