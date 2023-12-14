from typing import List
from pets_core.interactors.presenter_interfaces.get_adoption_requests_list_presenter_interface import \
    GetAdoptionRequestsListPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import WrongShelterId, ShelterNotFound
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import AdoptionRequestDTO, GetAdoptionRequestsListDTO


class GetAdoptionRequestsListInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_adoption_requests_list_wrapper(self, get_adoption_requests_list_dto: GetAdoptionRequestsListDTO,
                                           presenter: GetAdoptionRequestsListPresenterInterface) -> HttpResponse:
        try:
            adoption_request_dtos_list = self.get_adoption_requests_list(
                get_adoption_requests_list_dto=get_adoption_requests_list_dto)
        except ShelterNotFound:
            return presenter.raise_exception_for_shelter_not_found()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        return presenter.get_response_for_get_adoption_requests_list(
            requests_list_dto=adoption_request_dtos_list)

    def get_adoption_requests_list(self, get_adoption_requests_list_dto: GetAdoptionRequestsListDTO) -> List[
        AdoptionRequestDTO]:
        self.storage.validate_if_shelter_exists(shelter_id=get_adoption_requests_list_dto.shelter_id)
        self.storage.validate_if_user_is_shelter(shelter_id=get_adoption_requests_list_dto.shelter_id,
                                                 user_id=get_adoption_requests_list_dto.user_id)
        adoption_request_dtos_list = self.storage.get_adoption_requests_list(
            get_adoption_requests_list_dto=get_adoption_requests_list_dto)
        return adoption_request_dtos_list
