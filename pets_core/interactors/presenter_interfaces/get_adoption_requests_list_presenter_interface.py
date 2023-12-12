from typing import List
from abc import abstractmethod, ABC
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from django.http import HttpResponse


class GetAdoptionRequestsListPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_get_adoption_requests_list(self, adoption_request_dtos_list: List[
        AdoptionRequestDTO]) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_shelter_not_found(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
