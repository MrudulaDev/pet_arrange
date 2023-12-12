from typing import Dict, List
from pets_core.constants.exception_messages import SHELTER_NOT_FOUND, WRONG_SHELTER_ID
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.get_adoption_requests_list_presenter_interface import \
    GetAdoptionRequestsListPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(GetAdoptionRequestsListPresenterInterface, HTTPResponseMixin):

    def get_response_for_get_adoption_requests_list(self, requests_list_dto: List[AdoptionRequestDTO]) -> HttpResponse:
        adoption_requests_dict_list = self._get_request_details(requests_list_dto)
        return self.prepare_200_success_response(response_dict={"adoption_requests_list": adoption_requests_dict_list})

    @staticmethod
    def _get_request_details(requests_list_dto: List[AdoptionRequestDTO]) -> List[Dict]:
        requests_dict_list = []
        for request_dto in requests_list_dto:
            request_details_dict = {
                "request_id": request_dto.request_id,
                "request_status": request_dto.request_status,
                "pet_id": request_dto.pet_id,
                "adopter_id": request_dto.adopter_id,
                "requested_at": request_dto.requested_at
            }
            requests_dict_list += [request_details_dict]
        return requests_dict_list

    def raise_exception_for_shelter_not_found(self) -> HttpResponse:
        response_dict = {
            "response": SHELTER_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": SHELTER_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        response_dict = {
            "response": WRONG_SHELTER_ID[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": WRONG_SHELTER_ID[1]
        }
        return self.prepare_401_unauthorized_response(response_dict=response_dict)
