import factory
from datetime import datetime
from pets_core.interactors.storage_interfaces.dtos import UpdatePetDetailsDTO, PetDetailsDTO, GetPetsFilterParamsDTO, \
    CreateAdoptionRequestDTO, AdoptionRequestDTO, GetAdoptionRequestDTO
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus, RequestStatus
from pets_core.models.adopter import Adopter


class PetDetailsDTOFactory(factory.Factory):
    class Meta:
        model = PetDetailsDTO

    # todo: we should always use factory for details like ids, names
    pet_id = 1
    name = "husky"
    age = 1
    pet_category = PetCategory.DOG.value
    pet_size = PetSize.SMALL.value
    gender = PetGender.FEMALE.value
    status = PetStatus.AVAILABLE.value
    shelter_id = 1


class UpdatePetDetailsDTOFactory(factory.Factory):
    class Meta:
        model = UpdatePetDetailsDTO

    pet_id = 1
    name = "musky"
    age = 2
    pet_category = PetCategory.DOG.value
    pet_size = PetSize.SMALL.value
    gender = PetGender.FEMALE.value


class GetPetsFilterParamsDTOFactory(factory.Factory):
    class Meta:
        model = GetPetsFilterParamsDTO

    shelter_id = 1
    pet_category = PetCategory.CAT.value
    pet_size = PetSize.LARGE.value
    gender = PetGender.MALE.value


class CreateAdoptionRequestDTOFactory(factory.Factory):
    class Meta:
        model = CreateAdoptionRequestDTO

    user_id = "string"
    pet_id = 1


class AdoptionRequestDTOFactory(factory.Factory):
    class Meta:
        model = AdoptionRequestDTO

    request_id = 1
    request_status = RequestStatus.OPEN.value
    pet_id = 1
    adopter_id = 1
    requested_at = datetime.now()


class GetAdoptionRequestDTOFactory(factory.Factory):
    class Meta:
        model = GetAdoptionRequestDTO

    user_id = "string"
    request_id = 1