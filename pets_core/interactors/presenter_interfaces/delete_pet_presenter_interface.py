from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetIdDTO
from django.http import HttpResponse


class DeletePetPresenterInterface:
    @abstractmethod
    def get_response_for_delete_pet(self, pet_id_dto: PetIdDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
