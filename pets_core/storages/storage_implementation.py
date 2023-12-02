from ib_common.stores.key_store_v2 import DoesNotExist

from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId, PetIdAlreadyExists, \
    ShelterNotFound, PetNotFoundInShelter, NameAlreadyExists
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, GetPetsFilterParamsDTO
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from typing import List
from django.db.models import Q
from abc import ABC


class StorageImplementation(StorageInterface, ABC):

    def get_pet(self, pet_id: int) -> PetDetailsDTO:
        pet = Pet.objects.get(pet_id=pet_id)
        pet_dto = self._convert_pet_object_to_dto(pet=pet)
        return pet_dto

    def delete_pet(self, pet_id: int):
        pet = Pet.objects.get(pet_id=pet_id)
        pet.delete()

    def create_pet(self, pet_details_dto: PetDetailsDTO):
        pet_id = pet_details_dto.pet_id
        name = pet_details_dto.name
        age = pet_details_dto.age
        pet_category = pet_details_dto.pet_category
        gender = pet_details_dto.gender
        size = pet_details_dto.size
        shelter_id = pet_details_dto.shelter_id
        status = pet_details_dto.status
        Pet.objects.create(pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                           pet_category=pet_category, gender=gender, size=size, status=status)

    def update_pet(self, pet_details_dto: PetDetailsDTO) -> PetDetailsDTO:
        Pet.objects.filter(pet_id=pet_details_dto.pet_id).update(name=pet_details_dto.name, age=pet_details_dto.age,
                                                                 pet_category=pet_details_dto.pet_category,
                                                                 gender=pet_details_dto.gender,
                                                                 size=pet_details_dto.size)
        pet = Pet.objects.get(pet_id=pet_details_dto.pet_id)
        pet_dto = self._convert_pet_object_to_dto(pet=pet)
        return pet_dto

    def get_pets_list(self, filter_params: GetPetsFilterParamsDTO) -> List[PetDetailsDTO]:
        shelter_id = filter_params.shelter_id
        pet_category = filter_params.pet_category
        gender = filter_params.gender
        size = filter_params.size
        filters = Q(shelter_id=shelter_id)
        if pet_category is not None:
            filters &= Q(pet_category=pet_category)
        if gender is not None:
            filters &= Q(gender=gender)
        if size is not None:
            filters &= Q(size=size)
        pets_list = Pet.objects.filter(filters)
        pets_list_dto = self._convert_pet_objects_to_dto(pets_list=pets_list)
        return pets_list_dto

    def validate_pet_id(self, pet_id: int):
        is_valid_pet_id = Pet.objects.filter(pet_id=pet_id).exists()
        is_invalid_pet_id = not is_valid_pet_id

        if is_invalid_pet_id:
            raise InvalidPetId(pet_id=pet_id)

    def validate_user_access_to_pet_shelter(self, pet_id: int, user_id: int):
        pet = Pet.objects.filter(pet_id=pet_id).first()
        pet_shelter = pet.shelter
        user_shelter = Shelter.objects.get(user_id=user_id)

        if pet_shelter != user_shelter:
            raise WrongShelterId(shelter_id=user_shelter)

    def validate_if_pet_exists_in_user_shelter(self, pet_id: int, user_id: str):
        user_shelter = Shelter.objects.get(user_id=user_id)
        pet_ids_of_all_pets_in_shelter = Pet.objects.filter(shelter=user_shelter).values_list('pet_id', flat=True)
        if int(pet_id) not in pet_ids_of_all_pets_in_shelter:
            raise PetNotFoundInShelter(pet_id=pet_id)

    def validate_if_pet_name_already_exists(self, name: str):
        if name in Pet.objects.all().values_list('name', flat=True):
            raise NameAlreadyExists(name=name)

    def validate_if_pet_id_already_exists(self, pet_id: int):
        is_valid_pet_id = Pet.objects.filter(pet_id=pet_id).exists()

        if is_valid_pet_id:
            raise PetIdAlreadyExists(pet_id=pet_id)

    def validate_shelter_id_authorization_with_shelter_id(self, user_id: int, shelter_id: int):
        pet_shelter_id = shelter_id
        user_shelter = Shelter.objects.get(user_id=user_id)
        user_shelter_id = user_shelter.shelter_id

        if pet_shelter_id != user_shelter_id:
            raise WrongShelterId(shelter_id=user_shelter)

    def validate_if_shelter_exists(self, shelter_id: int):
        try:
            Shelter.objects.get(shelter_id=shelter_id)
        except DoesNotExist:
            raise ShelterNotFound(shelter_id=shelter_id)

    @staticmethod
    def _convert_pet_object_to_dto(pet: Pet) -> PetDetailsDTO:
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
    def _convert_pet_objects_to_dto(pets_list: List) -> List[PetDetailsDTO]:
        pets_list_dto = []
        for pet in pets_list:
            pet_dto = PetDetailsDTO(
                pet_id=pet.pet_id,
                name=pet.name,
                age=pet.age,
                pet_category=pet.pet_category,
                size=pet.size,
                gender=pet.gender,
                status=pet.status
            )
            pets_list_dto += [pet_dto]
        return pets_list_dto
