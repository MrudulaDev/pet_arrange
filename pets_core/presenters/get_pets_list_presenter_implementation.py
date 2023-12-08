from typing import Dict, List
from pets_core.constants.exception_messages import SHELTER_NOT_FOUND, WRONG_SHELTER_ID
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from pets_core.interactors.presenter_interfaces.get_pets_list_presenter_interface import GetPetsListPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import PetDetailsDTO
from pets_core.constants.enums import StatusCode
from django.http import HttpResponse


class GetPetsListPresenterImplementation(GetPetsListPresenterInterface, HTTPResponseMixin):

    def get_response_for_get_pets_list(self, pets_list_dto: List[PetDetailsDTO]) -> HttpResponse:
        pet_dict_list = self._get_pets_details(pets_list_dto)
        return self.prepare_200_success_response(response_dict={"all_pets": pet_dict_list})

    @staticmethod
    def _get_pets_details(pets_list_dto: List[PetDetailsDTO]) -> List[Dict]:
        pet_dict_list = []
        for pet_dto in pets_list_dto:
            pet_details_dict = {
                "pet_id": pet_dto.pet_id,
                "name": pet_dto.name,
                "age": pet_dto.age,
                "pet_category": pet_dto.pet_category,
                "pet_size": pet_dto.pet_size,
                "gender": pet_dto.gender,
                "status": pet_dto.status
            }
            pet_dict_list += [pet_details_dict]
        return pet_dict_list

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
