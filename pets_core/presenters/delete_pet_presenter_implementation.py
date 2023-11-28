from typing import Dict
from pets_core.constants.exception_messages import INVALID_PET_ID, WRONG_SHELTER_ID
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.delete_pet_presenter_interface import DeletePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import PetIdDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class PresenterImplementation(DeletePetPresenterInterface, HTTPResponseMixin):

    def get_response_for_delete_pet(self, pet_id_dto: PetIdDTO) -> HttpResponse:
        pet_id_dict = self._get_pet_id(pet_id_dto)
        return self.prepare_200_success_response(response_dict=pet_id_dict)

    @staticmethod
    def _get_pet_id(pet_id_dto: PetIdDTO) -> Dict:
        pet_id_dict = {
            "pet_id": pet_id_dto.pet_id
        }
        return pet_id_dict

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
