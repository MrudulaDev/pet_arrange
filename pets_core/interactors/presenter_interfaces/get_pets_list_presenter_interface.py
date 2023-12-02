from abc import abstractmethod, ABC
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from django.http import HttpResponse
from typing import List


class GetPetsListPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_get_pets_list(self, pets_list_dto: List[PetDetailsDTO]) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_shelter_not_found(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
