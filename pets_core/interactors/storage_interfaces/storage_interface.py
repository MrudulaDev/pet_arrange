from abc import abstractmethod
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, GetPetsFilterParamsDTO, UpdatePetDetailsDTO, \
    CreateAdoptionRequestDTO, AdoptionRequestDTO, GetAdoptionRequestDTO, ApproveAdoptionRequestDTO, \
    GetAdoptionRequestsListDTO
from typing import List


class StorageInterface:

    @abstractmethod
    def get_pet(self, pet_id: int) -> PetDetailsDTO:
        pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> int:
        pass

    @abstractmethod
    def create_pet(self, pet_details_dto: PetDetailsDTO) -> PetDetailsDTO:
        pass

    @abstractmethod
    def update_pet(self, pet_details_dto: UpdatePetDetailsDTO) -> UpdatePetDetailsDTO:
        pass

    @abstractmethod
    def get_pets_list(self, filter_params: GetPetsFilterParamsDTO) -> List[PetDetailsDTO]:
        pass

    @abstractmethod
    def create_adoption_request(self,
                                create_adoption_request_dto: CreateAdoptionRequestDTO,
                                adopter_id: int) -> AdoptionRequestDTO:
        pass

    @abstractmethod
    def validate_pet_id(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_user_access_to_pet_shelter(self, user_id: str, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_pet_id_already_exists(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_shelter_id_authorization_with_shelter_id(self, user_id: str, shelter_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_pet_exists_in_user_shelter(self, pet_id: int, user_id: str) -> None:
        pass

    @abstractmethod
    def validate_if_pet_name_already_exists(self, name: str) -> None:
        pass

    @abstractmethod
    def validate_if_shelter_exists(self, shelter_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_user_is_shelter(self, shelter_id: int, user_id: str) -> None:
        pass

    @abstractmethod
    def validate_if_pet_already_adopted(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_request_already_raised(self, pet_id: int, adopter_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_user_is_adopter(self, user_id: str) -> None:
        pass

    @abstractmethod
    def get_adopter_id(self, user_id: str) -> int:
        pass

    @abstractmethod
    def validate_adoption_request_id(self, request_id: int) -> None:
        pass

    @abstractmethod
    def get_adoption_request(self, get_adoption_request_dto: GetAdoptionRequestDTO) -> AdoptionRequestDTO:
        pass

    @abstractmethod
    def validate_adoption_request_already_approved_or_closed(self, request_id: int) -> None:
        pass


    @abstractmethod
    def close_all_adoption_requests_on_requested_pet(self, request_id: int) -> List:
        pass

    @abstractmethod
    def approve_adoption_request(self, approve_adoption_request_dto: ApproveAdoptionRequestDTO) -> AdoptionRequestDTO:
        pass

    @abstractmethod
    def get_adoption_requests_list(self, get_adoption_requests_list_dto: GetAdoptionRequestsListDTO) -> List[
        AdoptionRequestDTO]:
        pass
