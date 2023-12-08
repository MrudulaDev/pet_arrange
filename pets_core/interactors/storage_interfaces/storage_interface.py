from abc import abstractmethod
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, GetPetsFilterParamsDTO, UpdatePetDetailsDTO
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
