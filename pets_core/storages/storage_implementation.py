from pets_core.exceptions.custom_exceptions import InvalidPetId, WrongShelterId, PetIdAlreadyExists, \
    ShelterNotFound, PetNotFoundInShelter, NameAlreadyExists, UserIsNotAdopter, AdoptionRequestAlreadyRaised, \
    PetAlreadyAdopted, AdoptionRequestNotFound, AdoptionRequestAccessDenied, AdoptionRequestClosed, \
    AdoptionRequestAlreadyApproved
from pets_core.constants.enums import PetStatus, RequestStatus
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter
from pets_core.models.adopter import Adopter
from pets_core.models.request import Request
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, GetPetsFilterParamsDTO, UpdatePetDetailsDTO, \
    AdoptionRequestDTO, CreateAdoptionRequestDTO, GetAdoptionRequestDTO, ApproveAdoptionRequestDTO, \
    GetAdoptionRequestsListDTO
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from typing import List
from django.db.models import Q
from abc import ABC
from django.core.exceptions import ObjectDoesNotExist


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
        pet_category = pet_details_dto.pet_category
        gender = pet_details_dto.gender
        pet_size = pet_details_dto.pet_size
        shelter_id = pet_details_dto.shelter_id
        age = pet_details_dto.age
        status = pet_details_dto.status
        pet = Pet.objects.create(pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                 pet_category=pet_category, gender=gender, pet_size=pet_size, status=status)
        return pet

    def update_pet(self, pet_details_dto: PetDetailsDTO) -> UpdatePetDetailsDTO:
        Pet.objects.filter(pet_id=pet_details_dto.pet_id).update(name=pet_details_dto.name, age=pet_details_dto.age,
                                                                 pet_category=pet_details_dto.pet_category,
                                                                 gender=pet_details_dto.gender,
                                                                 pet_size=pet_details_dto.pet_size)
        pet = Pet.objects.get(pet_id=pet_details_dto.pet_id)
        pet_dto = self._convert_pet_object_to_dto(pet=pet)
        return pet_dto

    def get_pets_list(self, filter_params: GetPetsFilterParamsDTO) -> List[PetDetailsDTO]:
        shelter_id = filter_params.shelter_id
        pet_category = filter_params.pet_category
        gender = filter_params.gender
        pet_size = filter_params.pet_size
        filters = Q(shelter_id=shelter_id)
        if pet_category is not None:
            filters &= Q(pet_category=pet_category)
        if gender is not None:
            filters &= Q(gender=gender)
        if pet_size is not None:
            filters &= Q(pet_size=pet_size)
        filtered_pets_list = Pet.objects.filter(filters)
        pets_list_dto = self._convert_pet_objects_to_dto(pets_list=filtered_pets_list)
        return pets_list_dto

    def create_adoption_request(self, create_adoption_request_dto: CreateAdoptionRequestDTO,
                                adopter_id: int) -> AdoptionRequestDTO:
        request = Request(requested_by_id=adopter_id,
                          requested_pet_id=create_adoption_request_dto.pet_id)
        request.save()
        adoption_request_dto = self._convert_request_object_to_dto(request=request)
        return adoption_request_dto

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
        except:
            raise ShelterNotFound(shelter_id=shelter_id)

    def validate_if_pet_already_adopted(self, pet_id: int):
        status = Pet.objects.filter(pet_id=pet_id).values_list('status', flat=True).first()
        if status == PetStatus.ADOPTED.value:
            raise PetAlreadyAdopted(pet_id=pet_id)

    def validate_if_user_is_adopter(self, user_id: str):
        try:
            Adopter.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            raise UserIsNotAdopter(user_id=user_id)

    def get_adopter_id(self, user_id: str):
        adopter_id = Adopter.objects.filter(user_id=user_id).values_list('id', flat=True).first()
        return adopter_id

    def validate_if_request_already_raised(self, adopter_id: int, pet_id: int):
        if Request.objects.filter(requested_pet__pet_id=pet_id, requested_by__id=adopter_id).exists():
            request_id = Request.objects.filter(requested_pet__pet_id=pet_id, requested_by__id=adopter_id).values_list(
                'request_id', flat=True).first()
            raise AdoptionRequestAlreadyRaised(request_id=request_id)

    def validate_adoption_request_id(self, request_id: int):
        if not Request.objects.filter(request_id=request_id).exists():
            raise AdoptionRequestNotFound(request_id=request_id)

    def validate_adoption_request_access(self, request_id: int, user_id: str):
        # todo: This logic is more suited in interactor or a mixin,
        #  because we are handling with multiple tables here and some conditions
        request = Request.objects.get(request_id=request_id)
        pet = request.requested_pet
        adopter = request.requested_by
        requested_pet_shelter_user_id = pet.shelter.user_id
        requested_pet_adopter_user_id = adopter.user_id
        if user_id not in [requested_pet_shelter_user_id, requested_pet_adopter_user_id]:
            raise AdoptionRequestAccessDenied(user_id=user_id)

    def get_adoption_request(self, get_adoption_request_dto: GetAdoptionRequestDTO) -> AdoptionRequestDTO:
        request = Request.objects.get(request_id=get_adoption_request_dto.request_id)
        adoption_request_dto = self._convert_request_object_to_dto(request=request)
        return adoption_request_dto

    def validate_adoption_request_already_approved(self, request_id: int):
        request = Request.Objects.get(request_id=request_id)
        if request.request_status is RequestStatus.APPROVED.value:
            raise AdoptionRequestAlreadyApproved(request_id=request_id)

    def validate_adoption_request_closed(self, request_id: int):
        request = Request.Objects.get(request_id=request_id)
        if request.request_status is RequestStatus.CLOSED.value:
            raise AdoptionRequestClosed(request_id=request_id)

    def approve_adoption_request(self, approve_adoption_request_dto: ApproveAdoptionRequestDTO) -> AdoptionRequestDTO:
        request = Request.Objects.get(request_id=approve_adoption_request_dto.request_id)
        request.request_status = RequestStatus.APPROVED.value
        request.save()
        pet = request.requested_pet
        pet.status = PetStatus.ADOPTED.value
        pet.save()
        # todo: need to update `status_change_timestamp` value
        adoption_request_dto = self._convert_request_object_to_dto(request=request)
        return adoption_request_dto

    def close_all_other_adoption_requests_on_requested_pet(self, request_id: int):
        requested_pet = Request.objects.get(request_id=request_id).requested_pet
        # todo: we are closing the approved request also here, once check the query
        all_pet_requests = Request.Objects.filter(requested_pet=requested_pet)
        # todo: we can use filter.update here instead of iteratively saving all objects (This is a bad storage call because database will be hit multiple times),
        #  and we should also update `status_change_timestamp` value for all closed requests
        for each_request in all_pet_requests:
            if each_request.request_id is not request_id:
                each_request.request_status = RequestStatus.CLOSED.value
                each_request.save()

    def get_adoption_requests_list(self,
                                   get_adoption_requests_list_dto: GetAdoptionRequestsListDTO) -> List[
        AdoptionRequestDTO]:
        # todo: unnecessary join is being done in below query
        # todo: we are only filtering with shelter_id, what about pet_name and pet_category ?
        requests_in_shelter = Request.objects.filter(
            requested_pet__shelter__shelter_id=get_adoption_requests_list_dto.shelter_id)
        # todo: above results should be sorted by requested_at
        adoption_request_dtos_list = self._convert_request_objects_to_dtos_list(request_objs_list=requests_in_shelter)
        return adoption_request_dtos_list

    @staticmethod
    def _convert_pet_object_to_dto(pet: Pet) -> PetDetailsDTO:
        pet_dto = PetDetailsDTO(
            pet_id=pet.pet_id,
            name=pet.name,
            age=pet.age,
            pet_category=pet.pet_category,
            pet_size=pet.pet_size,
            gender=pet.gender,
            status=pet.status,
            shelter_id=pet.shelter
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
                pet_size=pet.pet_size,
                gender=pet.gender,
                status=pet.status,
                shelter_id=pet.shelter
            )
            pets_list_dto += [pet_dto]
        return pets_list_dto

    @staticmethod
    def _convert_request_object_to_dto(request: Request) -> AdoptionRequestDTO:
        adoption_request_dto = AdoptionRequestDTO(
            request_id=request.request_id,
            request_status=request.request_status,
            pet_id=request.requested_pet.pet_id,
            adopter_id=request.requested_by.id,
            requested_at=str(request.requested_at)
        )
        return adoption_request_dto

    @staticmethod
    def _convert_request_objects_to_dtos_list(request_objs_list: List) -> List[AdoptionRequestDTO]:
        request_dtos_list = []
        for request in request_objs_list:
            request_dto = AdoptionRequestDTO(
                request_id=request.request_id,
                request_status=request.request_status,
                pet_id=request.requested_pet,
                adopter_id=request.requested_by,
                requested_at=request.requested_at
            )
            request_dtos_list += [request_dto]
        return request_dtos_list
