from pets_core.interactors.presenter_interfaces.create_pet_presenter_interface import CreatePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import WrongShelterId, PetIdAlreadyExists, InvalidAge
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


class CreatePetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    # todo: a method should have at most 3 args to maintain readability, so wrap up extra args to DTO and
    #  age is optional and pet category is an enum, so we should update the typing as well properly here
    def create_pet_wrapper(self, user_id: str, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str,
                           gender: str,
                           size: str, presenter: CreatePetPresenterInterface) -> HttpResponse:
        try:
            pet_details_dto = self.create_pet(user_id=user_id, pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                              pet_category=pet_category, gender=gender, size=size)
        except PetIdAlreadyExists:
            return presenter.raise_exception_for_pet_id_already_exists()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        except InvalidAge:
            return presenter.raise_exception_for_invalid_age()
        return presenter.get_response_for_create_pet(
            pet_details_dto=pet_details_dto)

    # todo: a method should have at most 3 args to maintain readability, so wrap up extra args to DTO
    def create_pet(self, user_id: str, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str,
                   gender: str,
                   size: str) -> PetDetailsDTO:
        # todo: age validation should be done in interactor not storage
        self.storage.validate_age(age=age)
        self.storage.validate_if_pet_id_already_exists(pet_id=pet_id)
        self.storage.validate_shelter_id_authorization_with_shelter_id(user_id=user_id, shelter_id=shelter_id)
        # todo: method args should be in DTO
        pet_details_dto = self.storage.create_pet(pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                                  pet_category=pet_category, gender=gender, size=size)
        return pet_details_dto
