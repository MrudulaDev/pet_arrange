from pets_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import WrongShelterId, PetIdAlreadyExists
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


class CreatePetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_pet_wrapper(self, user_id: int, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str,
                           gender: str,
                           size: str, presenter: PresenterInterface) -> HttpResponse:
        try:
            pet_details_dto = self.create_pet(user_id=user_id, pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                              pet_category=pet_category, gender=gender, size=size)
        except PetIdAlreadyExists:
            return presenter.raise_exception_for_pet_id_already_exists()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        return presenter.get_response_for_create_pet(
            pet_details_dto=pet_details_dto)

    def create_pet(self, user_id: int, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str,
                   gender: str,
                   size: str) -> PetDetailsDTO:
        self.storage.validate_if_pet_id_already_exists(pet_id=pet_id)
        self.storage.validate_shelter_id_with_shelter_id(user_id=user_id, shelter_id=shelter_id)
        pet_details_dto = \
            self.storage.create_pet(pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                    pet_category=pet_category, gender=gender, size=size)
        return pet_details_dto
