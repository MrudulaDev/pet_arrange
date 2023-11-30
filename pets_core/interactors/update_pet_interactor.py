from pets_core.interactors.presenter_interfaces.update_pet_presenter_interface import UpdatePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import PetNotFoundInShelter, InvalidAge, NameAlreadyExists
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


class UpdatePetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_pet_wrapper(self, user_id: str, pet_id: int, name: str, age: int, pet_category: str,
                           gender: str, size: str, presenter: UpdatePetPresenterInterface) -> HttpResponse:
        try:
            pet_details_dto = self.update_pet(user_id=user_id, pet_id=pet_id, name=name, age=age,
                                              pet_category=pet_category, gender=gender, size=size)
        except NameAlreadyExists:
            return presenter.raise_exception_for_name_already_exists()
        except PetNotFoundInShelter:
            return presenter.raise_exception_for_pet_not_found_in_shelter()
        except InvalidAge:
            return presenter.raise_exception_for_invalid_age()
        return presenter.get_response_for_update_pet(
            pet_details_dto=pet_details_dto)

    def update_pet(self, user_id: str, pet_id: int, name: str, age: int, pet_category: str,
                   gender: str,
                   size: str) -> PetDetailsDTO:
        #todo: method name and args are not in sync
        self.storage.validate_if_pet_exists_in_shelter(pet_id=pet_id, user_id=user_id)
        self.storage.validate_age(age=age)
        #todo: better to be specific about the name here, i.e, pet name or shelter name
        self.storage.validate_if_name_already_exists(name=name)
        pet_details_dto = self.storage.update_pet(pet_id=pet_id, name=name, age=age,
                                                  pet_category=pet_category, gender=gender, size=size)
        return pet_details_dto
