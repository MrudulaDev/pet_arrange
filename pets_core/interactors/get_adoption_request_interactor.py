from pets_core.interactors.presenter_interfaces.get_adoption_request_presenter_interface import \
    GetAdoptionRequestPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound, AdoptionRequestAccessDenied
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import AdoptionRequestDTO, GetAdoptionRequestDTO


class GetAdoptionRequestInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_adoption_request_wrapper(self, get_adoption_request_dto: GetAdoptionRequestDTO,
                                     presenter: GetAdoptionRequestPresenterInterface) -> HttpResponse:
        try:
            adoption_request_dto = self.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)
        except AdoptionRequestNotFound:
            return presenter.raise_exception_for_request_not_found()
        except AdoptionRequestAccessDenied:
            return presenter.raise_exception_for_request_access_denied()
        return presenter.get_response_for_get_adoption_request(adoption_request_dto=adoption_request_dto)

    def get_adoption_request(self, get_adoption_request_dto) -> AdoptionRequestDTO:
        self.storage.validate_adoption_request_id(request_id=get_adoption_request_dto.request_id)
        self.storage.validate_adoption_request_access(request_id=get_adoption_request_dto.request_id,
                                                      user_id=get_adoption_request_dto.user_id)
        adoption_request_dto = self.storage.get_adoption_request(get_adoption_request_dto=get_adoption_request_dto)
        return adoption_request_dto
