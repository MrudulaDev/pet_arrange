from abc import abstractmethod
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, PetIdDTO
from typing import List


class StorageInterface:

    @abstractmethod
    def get_pet(self, pet_id: str) -> PetDetailsDTO:
        pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> PetIdDTO:
        pass

    @abstractmethod
    def create_pet(self, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str, gender: str,
                   size: str) -> PetDetailsDTO:
        pass

    @abstractmethod
    def update_pet(self, pet_id: int, name: str, age: int, pet_category: str, gender: str,
                   size: str) -> PetDetailsDTO:
        pass

    @abstractmethod
    def get_pets_list(self, shelter_id: int, pet_category: str, gender: str,
                      size: str) -> List[PetDetailsDTO]:
        pass

    @abstractmethod
    def validate_pet_id(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_shelter_id(self, user_id: str, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_pet_id_already_exists(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_shelter_id_authorization_with_shelter_id(self, user_id: str, shelter_id: int) -> None:
        pass

    @abstractmethod
    def validate_age(self, age: int) -> None:
        pass

    @abstractmethod
    def validate_if_pet_exists_in_shelter(self, pet_id: int, user_id: str) -> None:
        pass

    @abstractmethod
    def validate_if_name_already_exists(self, name: str) -> None:
        pass

    @abstractmethod
    def validate_if_shelter_exists(self, shelter_id: int) -> None:
        pass
