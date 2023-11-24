from abc import abstractmethod
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, PetIdDTO


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
    def validate_pet_id(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_shelter_id(self, user_id: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_existing_shelter_id(self, shelter_id: int) -> None:
        pass

    @abstractmethod
    def validate_if_pet_id_already_exists(self, pet_id: int) -> None:
        pass

    @abstractmethod
    def validate_shelter_id_with_shelter_id(self, user_id: int, shelter_id: int) -> None:
        pass
