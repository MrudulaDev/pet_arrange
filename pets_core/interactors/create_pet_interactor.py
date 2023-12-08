from pets_core.interactors.presenter_interfaces.create_pet_presenter_interface import CreatePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import WrongShelterId, PetIdAlreadyExists, InvalidAge
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


class CreatePetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_pet_wrapper(self, user_id: str, pet_details_dto: PetDetailsDTO,
                           presenter: CreatePetPresenterInterface) -> HttpResponse:
        try:
            self.create_pet(user_id=user_id, pet_details_dto=pet_details_dto)
        except PetIdAlreadyExists:
            return presenter.raise_exception_for_pet_id_already_exists()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        except InvalidAge:
            return presenter.raise_exception_for_invalid_age()
        return presenter.get_response_for_create_pet(
            pet_details_dto=pet_details_dto)

    def create_pet(self, user_id: str, pet_details_dto: PetDetailsDTO) -> PetDetailsDTO:
        self.validate_age(age=pet_details_dto.age)
        self.storage.validate_if_pet_id_already_exists(pet_id=pet_details_dto.pet_id)
        self.storage.validate_shelter_id_authorization_with_shelter_id(user_id=user_id,
                                                                       shelter_id=pet_details_dto.shelter_id)
        self.storage.create_pet(pet_details_dto=pet_details_dto)
        return pet_details_dto

    @staticmethod
    def validate_age(age: int) -> None:
        if age is not None:
            if age <= 0:
                raise InvalidAge(age=age)
