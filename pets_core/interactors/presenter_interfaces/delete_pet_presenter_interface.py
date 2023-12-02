from abc import abstractmethod, ABC
from django.http import HttpResponse


class DeletePetPresenterInterface(ABC):
    @abstractmethod
    def get_response_for_delete_pet(self, pet_id: int) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        pass
