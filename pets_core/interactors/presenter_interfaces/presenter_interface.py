from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO, PetIdDTO
from django.http import HttpResponse


class PresenterInterface:

    @abstractmethod
    def get_response_for_get_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pass

    @abstractmethod
    def get_response_for_delete_pet(self, pet_id_dto: PetIdDTO) -> HttpResponse:
        pass

    @abstractmethod
    def get_response_for_create_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_pet_id_already_exists(self) -> HttpResponse:
        pass
