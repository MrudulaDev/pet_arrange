from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from django.http import HttpResponse


class UpdatePetPresenterInterface:
    @abstractmethod
    def get_response_for_update_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_age(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_pet_not_found_in_shelter(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_name_already_exists(self) -> HttpResponse:
        pass
