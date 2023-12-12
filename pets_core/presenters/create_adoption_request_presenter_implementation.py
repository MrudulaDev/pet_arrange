from typing import Dict
from pets_core.constants.exception_messages import INVALID_PET_ID, PET_ALREADY_ADOPTED, ADOPTION_REQUEST_ALREADY_RAISED, \
    USER_IS_NOT_ADOPTER
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.create_adoption_request_presenter_interface import \
    CreateAdoptionRequestPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import AdoptionRequestDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(CreateAdoptionRequestPresenterInterface, HTTPResponseMixin):

    def get_response_for_create_adoption_request(self, adoption_request_dto: AdoptionRequestDTO) -> HttpResponse:
        adoption_request_dict = self._create_adoption_request_details(adoption_request_dto)
        return self.prepare_201_created_response(response_dict=adoption_request_dict)

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

    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_PET_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_PET_ID[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_pet_already_adopted(self) -> HttpResponse:
        response_dict = {
            "response": PET_ALREADY_ADOPTED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PET_ALREADY_ADOPTED[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_user_is_not_adopter(self) -> HttpResponse:
        response_dict = {
            "response": USER_IS_NOT_ADOPTER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_IS_NOT_ADOPTER[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_adoption_request_already_raised(self) -> HttpResponse:
        response_dict = {
            "response": ADOPTION_REQUEST_ALREADY_RAISED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ADOPTION_REQUEST_ALREADY_RAISED[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)
