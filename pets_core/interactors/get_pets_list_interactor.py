from pets_core.interactors.presenter_interfaces.get_pets_list_presenter_interface import GetPetsListPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import ShelterNotFound, WrongShelterId
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import GetPetsFilterParamsDTO, PetDetailsDTO
from typing import List
from pets_core.models.pet import Pet


class GetPetsListInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_pets_list_wrapper(self, user_id: str, filter_params: GetPetsFilterParamsDTO,
                              presenter: GetPetsListPresenterInterface) -> HttpResponse:
        try:
            pets_list_dto = self.get_pets_list(user_id=user_id, filter_params=filter_params)
        except ShelterNotFound:
            return presenter.raise_exception_for_shelter_not_found()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        return presenter.get_response_for_get_pets_list(
            pets_list_dto=pets_list_dto)

    def get_pets_list(self, user_id: str, filter_params: GetPetsFilterParamsDTO) -> List[PetDetailsDTO]:
        self.storage.validate_if_shelter_exists(shelter_id=filter_params.shelter_id)
        self.storage.validate_shelter_id_authorization_with_shelter_id(shelter_id=filter_params.shelter_id,
                                                                       user_id=user_id)
        pets_list= Pet.objects.all()
        pets_list_dto = self.storage.get_pets_list(filter_params=filter_params)
        return pets_list_dto
