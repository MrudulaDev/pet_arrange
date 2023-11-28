from pets_core.interactors.presenter_interfaces.get_pet_presenter_interface import GetPetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


class GetPetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_pet_wrapper(self, user_id: str, pet_id: str, presenter: GetPetPresenterInterface) -> HttpResponse:
        try:
            pet_details_dto = self.get_pet(pet_id=pet_id, user_id=user_id)
        except InvalidPetId:
            return presenter.raise_exception_for_invalid_pet()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        return presenter.get_response_for_get_pet(
            pet_details_dto=pet_details_dto)

    def get_pet(self, user_id: str, pet_id: str) -> PetDetailsDTO:
        self.storage.validate_pet_id(pet_id=pet_id)
        self.storage.validate_shelter_id(pet_id=pet_id,user_id=user_id)
        pet_details_dto = \
            self.storage.get_pet(pet_id=pet_id)
        return pet_details_dto
