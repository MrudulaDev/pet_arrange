from typing import Dict
from pets_core.constants.exception_messages import ADOPTION_REQUEST_ACCESS_DENIED, ADOPTION_REQUEST_NOT_FOUND
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.get_adoption_request_presenter_interface import \
    GetAdoptionRequestPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(GetAdoptionRequestPresenterInterface, HTTPResponseMixin):

    def get_response_for_get_adoption_request(self, adoption_request_dto: AdoptionRequestDTO) -> HttpResponse:
        adoption_request_dict = self._create_adoption_request_details(adoption_request_dto)
        return self.prepare_200_success_response(response_dict=adoption_request_dict)

    @staticmethod
    def _create_adoption_request_details(adoption_request_dto: AdoptionRequestDTO) -> Dict:
        pet_details_dict = {
            "request_id": adoption_request_dto.request_id,
            "request_status": adoption_request_dto.request_status,
            "pet_id": adoption_request_dto.pet_id,
            "adopter_id": adoption_request_dto.adopter_id,
            "requested_at": adoption_request_dto.requested_at
        }
        return pet_details_dict

    def raise_exception_for_request_not_found(self) -> HttpResponse:
        response_dict = {
            "response": ADOPTION_REQUEST_NOT_FOUND[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ADOPTION_REQUEST_NOT_FOUND[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_request_access_denied(self) -> HttpResponse:
        response_dict = {
            "response": ADOPTION_REQUEST_ACCESS_DENIED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ADOPTION_REQUEST_ACCESS_DENIED[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)
