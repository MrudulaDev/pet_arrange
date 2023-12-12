from abc import abstractmethod, ABC
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from django.http import HttpResponse


class CreateAdoptionRequestPresenterInterface(ABC):

    @abstractmethod
    def get_response_for_create_adoption_request(self, adoption_request_dto: AdoptionRequestDTO) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_pet_already_adopted(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_user_is_not_adopter(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_adoption_request_already_raised(self) -> HttpResponse:
        pass
