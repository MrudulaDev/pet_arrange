import pytest

from pets_core.models.pet import Pet
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import GetPetsFilterParamsDTOFactory


class TestGetPetsList:
    @pytest.mark.django_db
    def test_with_all_valid_values_in_filter_params(self, create_shelters_and_pets_in_them_return_pets_list):
        # Arrange
        storage = StorageImplementation()
        pets_list = create_shelters_and_pets_in_them_return_pets_list
        filter_params = GetPetsFilterParamsDTOFactory()
        filtered_pets = [pet for pet in pets_list if all([
            (filter_params.shelter_id is None or pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or pet.pet_category == filter_params.pet_category),
            (filter_params.pet_size is None or pet.pet_size == filter_params.pet_size),
            (filter_params.gender is None or pet.gender == filter_params.gender),
        ])]

        # Act
        pet_dtos_list = storage.get_pets_list(filter_params)

        # Assert
        assert filtered_pets == pet_dtos_list

    @pytest.mark.django_db
    def test_with_all_null_values_in_filter_params(self, create_shelters_and_pets_in_them_return_pets_list):
        # Arrange
        storage = StorageImplementation()
        pets_list = create_shelters_and_pets_in_them_return_pets_list
        filter_params = GetPetsFilterParamsDTOFactory(pet_category=None, pet_size=None, gender=None)
        filtered_pets = [pet for pet in pets_list if all([
            (filter_params.shelter_id is None or pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or pet.pet_category == filter_params.pet_category),
            (filter_params.pet_size is None or pet.pet_size == filter_params.pet_size),
            (filter_params.gender is None or pet.gender == filter_params.gender),
        ])]
        filtered_pets_dtos = storage._convert_pet_objects_to_dto(filtered_pets)
        # Act
        pet_dtos_list = storage.get_pets_list(filter_params)

        # Assert
        assert filtered_pets_dtos == pet_dtos_list

    @pytest.mark.django_db
    def test_with_combination_of_null_and_non_null_values(self,
                                                          create_shelters_and_pets_in_them_return_pets_list):
        # Arrange
        storage = StorageImplementation()
        pets_list = create_shelters_and_pets_in_them_return_pets_list
        filter_params = GetPetsFilterParamsDTOFactory(pet_size=None, gender=None)
        filtered_pets = [pet for pet in pets_list if all([
            (filter_params.shelter_id is None or pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or pet.pet_category == filter_params.pet_category),
            (filter_params.pet_size is None or pet.pet_size == filter_params.pet_size),
            (filter_params.gender is None or pet.gender == filter_params.gender),
        ])]
        filtered_pets_dtos = storage._convert_pet_objects_to_dto(filtered_pets)
        # Act
        pet_dtos_list = storage.get_pets_list(filter_params)

        # Assert
        assert filtered_pets_dtos == pet_dtos_list