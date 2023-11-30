from abc import abstractmethod
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from django.http import HttpResponse
from typing import List

# todo: should inherit abc.ABC class to interface
class GetPetsListPresenterInterface:

    @abstractmethod
    def get_response_for_get_pets_list(self, pets_list_dto: List[PetDetailsDTO]) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_shelter_not_found(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
