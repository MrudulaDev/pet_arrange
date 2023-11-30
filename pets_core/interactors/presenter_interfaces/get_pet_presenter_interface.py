from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from django.http import HttpResponse

# todo: should inherit abc.ABC class to interface
class GetPetPresenterInterface:

    @abstractmethod
    def get_response_for_get_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
