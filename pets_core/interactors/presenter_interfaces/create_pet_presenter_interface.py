from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from django.http import HttpResponse

# todo: should inherit abc.ABC class to interface
class CreatePetPresenterInterface:

    @abstractmethod
    def get_response_for_create_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_age(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_pet_id_already_exists(self) -> HttpResponse:
        pass

