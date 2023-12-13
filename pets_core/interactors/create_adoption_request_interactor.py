from pets_core.interactors.presenter_interfaces.create_adoption_request_presenter_interface import \
    CreateAdoptionRequestPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import InvalidPetId, PetAlreadyAdopted, AdoptionRequestAlreadyRaised, \
    UserIsNotAdopter
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import CreateAdoptionRequestDTO, AdoptionRequestDTO


class CreateAdoptionRequestInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_adoption_request_wrapper(self, create_adoption_request_dto: CreateAdoptionRequestDTO,
                                        presenter: CreateAdoptionRequestPresenterInterface) -> HttpResponse:
        try:
            adoption_request_dto = self.create_adoption_request(create_adoption_request_dto=create_adoption_request_dto)
        except InvalidPetId:
            return presenter.raise_exception_for_invalid_pet()
        except PetAlreadyAdopted:
            return presenter.raise_exception_for_pet_already_adopted()
        except UserIsNotAdopter:
            return presenter.raise_exception_for_user_is_not_adopter()
        except AdoptionRequestAlreadyRaised:
            return presenter.raise_exception_for_adoption_request_already_raised()
        return presenter.get_response_for_create_adoption_request(adoption_request_dto=adoption_request_dto)

    def create_adoption_request(self, create_adoption_request_dto) -> AdoptionRequestDTO:
        # todo: typing missed in input args
        self.storage.validate_pet_id(pet_id=create_adoption_request_dto.pet_id)
        self.storage.validate_if_pet_already_adopted(pet_id=create_adoption_request_dto.pet_id)
        self.storage.validate_if_user_is_adopter(user_id=create_adoption_request_dto.user_id)
        adopter_id = self.storage.get_adopter_id(user_id=create_adoption_request_dto.user_id)
        # todo: what if request is approved and adopter try to raise request again ?
        #  what is the expected behavior here ?
        self.storage.validate_if_request_already_raised(adopter_id=adopter_id,
                                                        pet_id=create_adoption_request_dto.pet_id)
        adoption_request_dto = self.storage.create_adoption_request(
            create_adoption_request_dto=create_adoption_request_dto, adopter_id=adopter_id)
        return adoption_request_dto
