from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId, PetIdAlreadyExists
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, PetIdDTO
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def get_pet(self, pet_id: int) -> PetDetailsDTO:
        pet = Pet.objects.get(pet_id=pet_id)
        pet_dto = self._convert_pet_object_to_dto(pet=pet)
        return pet_dto

    def delete_pet(self, pet_id: int) -> PetIdDTO:
        pet = Pet.objects.get(pet_id=pet_id)
        pet_id_dto = self._convert_pet_object_to_pet_id_dto(pet=pet)
        pet.delete()
        return pet_id_dto

    def create_pet(self, shelter_id: int, pet_id: int, name: str, age: int, pet_category: str, gender: str,
                   size: str) -> PetDetailsDTO:
        pet = Pet.objects.create(pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                 pet_category=pet_category, gender=gender, size=size)
        pet_dto = self._convert_pet_object_to_dto(pet=pet)
        return pet_dto

    def validate_pet_id(self, pet_id: int):
        is_valid_pet_id = Pet.objects.filter(pet_id=pet_id).exists()
        is_invalid_pet_id = not is_valid_pet_id

        if is_invalid_pet_id:
            raise InvalidPetId(pet_id=pet_id)

    def validate_shelter_id(self, pet_id: int, user_id: int):
        pet = Pet.objects.filter(pet_id=pet_id).first()
        pet_shelter = pet.shelter
        user_shelter = Shelter.objects.get(user_id=user_id)

        if pet_shelter != user_shelter:
            raise WrongShelterId(shelter_id=user_shelter)

    def validate_if_pet_id_already_exists(self, pet_id: int):
        is_valid_pet_id = Pet.objects.filter(pet_id=pet_id).exists()

        if is_valid_pet_id:
            raise PetIdAlreadyExists(pet_id=pet_id)

    def validate_shelter_id_with_shelter_id(self, user_id: int, shelter_id: int):
        pet_shelter = shelter_id
        user_shelter = Shelter.objects.get(user_id=user_id)

        if pet_shelter != user_shelter:
            raise WrongShelterId(shelter_id=user_shelter)

    @staticmethod
    def _convert_pet_object_to_dto(pet: Pet):
        pet_dto = PetDetailsDTO(
            pet_id=pet.pet_id,
            name=pet.name,
            age=pet.age,
            pet_category=pet.pet_category,
            size=pet.size,
            gender=pet.gender,
            status=pet.status
        )
        return pet_dto

    @staticmethod
    def _convert_pet_object_to_pet_id_dto(pet: Pet):
        pet_id_dto = PetIdDTO(
            pet_id=pet.pet_id
        )
        return pet_id_dto
