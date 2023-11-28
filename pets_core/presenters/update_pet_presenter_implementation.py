from typing import Dict
from pets_core.constants.exception_messages import PET_NOT_FOUND_IN_SHELTER, NAME_ALREADY_IN_USE, INVALID_AGE
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.update_pet_presenter_interface import UpdatePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(UpdatePetPresenterInterface, HTTPResponseMixin):

    def get_response_for_update_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pet_details_dict = self._update_pet_details(pet_details_dto)
        return self.prepare_200_success_response(response_dict=pet_details_dict)

    @staticmethod
    def _update_pet_details(pet_dto: PetDetailsDTO) -> Dict:
        pet_details_dict = {
            "pet_id": pet_dto.pet_id,
            "name": pet_dto.name,
            "age": pet_dto.age,
            "pet_category": pet_dto.pet_category,
            "size": pet_dto.size,
            "gender": pet_dto.gender,
            "status": pet_dto.status
        }
        return pet_details_dict

    def raise_exception_for_name_already_exists(self) -> HttpResponse:
        response_dict = {
            "response": NAME_ALREADY_IN_USE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": NAME_ALREADY_IN_USE[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_pet_not_found_in_shelter(self) -> HttpResponse:
        response_dict = {
            "response": PET_NOT_FOUND_IN_SHELTER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PET_NOT_FOUND_IN_SHELTER[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_exception_for_invalid_age(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_AGE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AGE[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)
