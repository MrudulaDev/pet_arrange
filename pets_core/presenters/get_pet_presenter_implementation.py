from typing import Dict
from pets_core.constants.exception_messages import INVALID_PET_ID, WRONG_SHELTER_ID
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.get_pet_presenter_interface import GetPetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(GetPetPresenterInterface, HTTPResponseMixin):

    def get_response_for_get_pet(self, pet_details_dto: PetDetailsDTO) -> HttpResponse:
        pet_details_dict = self._get_pet_details(pet_details_dto)
        return self.prepare_200_success_response(response_dict=pet_details_dict)

    @staticmethod
    def _get_pet_details(pet_dto: PetDetailsDTO) -> Dict:
        pet_details_dict = {
            "pet_id": pet_dto.pet_id,
            "name": pet_dto.name,
            "age": pet_dto.age,
            "pet_category": pet_dto.pet_category,
            "pet_size": pet_dto.pet_size,
            "gender": pet_dto.gender,
            "status": pet_dto.status
        }
        return pet_details_dict

    def raise_exception_for_invalid_pet(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_PET_ID[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_PET_ID[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_wrong_shelter(self) -> HttpResponse:
        response_dict = {
            "response": WRONG_SHELTER_ID[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": WRONG_SHELTER_ID[1]
        }
        return self.prepare_401_unauthorized_response(response_dict=response_dict)
