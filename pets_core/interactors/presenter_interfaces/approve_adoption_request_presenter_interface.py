from abc import abstractmethod, ABC
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from django.http import HttpResponse


class ApproveAdoptionRequestPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_approve_adoption_request(self, adoption_request_dto: AdoptionRequestDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_request_not_found(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_request_access_denied(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_request_already_approved(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_request_closed(self) -> HttpResponse:
        pass
