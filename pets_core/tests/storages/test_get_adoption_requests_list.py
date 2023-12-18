import pytest
from freezegun import freeze_time
from datetime import datetime
from django.db.models import Q
from pets_core.models.request import Request
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.tests.factories.storage_dtos import GetAdoptionRequestsListDTOFactory, AdoptionRequestDTOFactory
from pets_core.tests.factories.models import RequestFactory
from pets_core.models.pet import Pet
from pets_core.models.request import Request
from pets_core.models.adopter import Adopter


class TestGetRequestsList:
    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_all_values_in_filter_params(self, create_shelters_and_pets, load_adopters):
        # Arrange
        storage = StorageImplementation()
        requested_pet = Pet.objects.get(pet_id=1)
        requested_by_1 = Adopter.objects.get(id=1)
        requested_by_2 = Adopter.objects.get(id=2)
        request_1 = RequestFactory(request_id=1, requested_pet=requested_pet, requested_by=requested_by_1)
        request_1 = RequestFactory(request_id=2, requested_pet=requested_pet, requested_by=requested_by_2)
        requests_list = Request.objects.all()
        filter_params = GetAdoptionRequestsListDTOFactory()
        filtered_requests = [request for request in requests_list if all([
            (filter_params.shelter_id is None or request.requested_pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or request.requested_pet.pet_category == filter_params.pet_category),
            (filter_params.name is None or request.requested_pet.name == filter_params.name)
        ])]
        expected_requests_dto_list = []
        for request in filtered_requests:
            request_dto = AdoptionRequestDTOFactory(request_id=request.request_id, pet_id=request.requested_pet_id,
                                                    adopter_id=request.requested_by.id,
                                                    request_status=request.request_status,
                                                    requested_at=str(datetime.now()))

            expected_requests_dto_list += [request_dto]

        # Act
        adoption_request_dtos_list = storage.get_adoption_requests_list(filter_params)

        # Assert
        assert expected_requests_dto_list == adoption_request_dtos_list

    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_null_values_in_filter_params(self,create_shelters_and_pets, load_adopters ):
        # Arrange
        storage = StorageImplementation()
        requested_pet = Pet.objects.get(pet_id=1)
        requested_by_1 = Adopter.objects.get(id=1)
        requested_by_2 = Adopter.objects.get(id=2)
        request_1 = RequestFactory(request_id=1, requested_pet=requested_pet, requested_by=requested_by_1)
        request_1 = RequestFactory(request_id=2, requested_pet=requested_pet, requested_by=requested_by_2)
        requests_list = Request.objects.all()
        filter_params = GetAdoptionRequestsListDTOFactory(name= None, pet_category = None)
        filtered_requests = [request for request in requests_list if all([
            (filter_params.shelter_id is None or request.requested_pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or request.requested_pet.pet_category == filter_params.pet_category),
            (filter_params.name is None or request.requested_pet.name == filter_params.name)
        ])]
        expected_requests_dto_list = []
        for request in filtered_requests:
            request_dto = AdoptionRequestDTOFactory(request_id=request.request_id, pet_id=request.requested_pet_id,
                                                    adopter_id=request.requested_by.id,
                                                    request_status=request.request_status,
                                                    requested_at=str(datetime.now()))

            expected_requests_dto_list += [request_dto]

        # Act
        adoption_request_dtos_list = storage.get_adoption_requests_list(filter_params)

        # Assert
        assert expected_requests_dto_list == adoption_request_dtos_list

    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_combo_of_null_and_non_null_values_in_filter_params(self,create_shelters_and_pets, load_adopters ):
        # Arrange
        storage = StorageImplementation()
        requested_pet = Pet.objects.get(pet_id=1)
        requested_by_1 = Adopter.objects.get(id=1)
        requested_by_2 = Adopter.objects.get(id=2)
        request_1 = RequestFactory(request_id=1, requested_pet=requested_pet, requested_by=requested_by_1)
        request_1 = RequestFactory(request_id=2, requested_pet=requested_pet, requested_by=requested_by_2)
        requests_list = Request.objects.all()
        filter_params = GetAdoptionRequestsListDTOFactory(pet_category=None)
        filtered_requests = [request for request in requests_list if all([
            (filter_params.shelter_id is None or request.requested_pet.shelter_id == filter_params.shelter_id),
            (filter_params.pet_category is None or request.requested_pet.pet_category == filter_params.pet_category),
            (filter_params.name is None or request.requested_pet.name == filter_params.name)
        ])]
        expected_requests_dto_list = []
        for request in filtered_requests:
            request_dto = AdoptionRequestDTOFactory(request_id=request.request_id, pet_id=request.requested_pet_id,
                                                    adopter_id=request.requested_by.id,
                                                    request_status=request.request_status,
                                                    requested_at=str(datetime.now()))

            expected_requests_dto_list += [request_dto]

        # Act
        adoption_request_dtos_list = storage.get_adoption_requests_list(filter_params)

        # Assert
        assert expected_requests_dto_list == adoption_request_dtos_list