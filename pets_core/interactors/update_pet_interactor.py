from pets_core.interactors.presenter_interfaces.update_pet_presenter_interface import UpdatePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.interactors.create_pet_interactor import CreatePetInteractor
from pets_core.exceptions.custom_exceptions import PetNotFoundInShelter, InvalidAge, NameAlreadyExists
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import UpdatePetDetailsDTO


class PetValidationMixin:

    def validate_age(self, age: int):
        pass

    def validate_pet_shelter_owner(self, user_id: str, pet_id: str, storage: StorageInterface):
        #todo: get user shelter
        #todo: get pet shelter
        #if user_shelter != pet_shelter:
        pass


class UpdatePetInteractor(PetValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_pet_wrapper(self, user_id: str, pet_details_dto: UpdatePetDetailsDTO,
                           presenter: UpdatePetPresenterInterface) -> HttpResponse:
        try:
            pet_details_dto = self.update_pet(user_id=user_id, pet_details_dto=pet_details_dto)
        except NameAlreadyExists:
            return presenter.raise_exception_for_name_already_exists()
        except PetNotFoundInShelter:
            return presenter.raise_exception_for_pet_not_found_in_shelter()
        except InvalidAge:
            return presenter.raise_exception_for_invalid_age()
        return presenter.get_response_for_update_pet(
            pet_details_dto=pet_details_dto)

    def update_pet(self, user_id: str, pet_details_dto: UpdatePetDetailsDTO) -> UpdatePetDetailsDTO:
        self.storage.validate_if_pet_exists_in_user_shelter(pet_id=pet_details_dto.pet_id, user_id=user_id)
        self.storage.validate_if_pet_name_already_exists(name=pet_details_dto.name)
        create_pet_interactor = CreatePetInteractor(storage=self.storage)
        create_pet_interactor.validate_age(age=pet_details_dto.age)
        pet_details_dto = self.storage.update_pet(pet_details_dto)
        return pet_details_dto

