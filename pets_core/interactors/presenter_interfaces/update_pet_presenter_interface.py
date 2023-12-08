from abc import abstractmethod, ABC
from pets_core.interactors.storage_interfaces.storage_interface import UpdatePetDetailsDTO
from django.http import HttpResponse


class UpdatePetPresenterInterface(ABC):
    @abstractmethod
    def get_response_for_update_pet(self, pet_details_dto: UpdatePetDetailsDTO) -> HttpResponse:
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
