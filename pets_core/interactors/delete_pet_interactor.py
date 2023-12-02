from pets_core.interactors.presenter_interfaces.delete_pet_presenter_interface import DeletePetPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId
from django.http import HttpResponse


class DeletePetInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_pet_wrapper(self, user_id: str, pet_id: int, presenter: DeletePetPresenterInterface) -> HttpResponse:
        try:
            pet_id_dto = self.delete_pet(pet_id=pet_id, user_id=user_id)
        except InvalidPetId:
            return presenter.raise_exception_for_invalid_pet()
        except WrongShelterId:
            return presenter.raise_exception_for_wrong_shelter()
        return presenter.get_response_for_delete_pet(
            pet_id=pet_id)

    def delete_pet(self, user_id: str, pet_id: int) -> int:
        self.storage.validate_pet_id(pet_id=pet_id)
        self.storage.validate_user_access_to_pet_shelter(pet_id=pet_id, user_id=user_id)
        self.storage.delete_pet(pet_id=pet_id)
        return pet_id
