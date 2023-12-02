from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO, GetPetsFilterParamsDTO
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus
import factory


class PetDetailsDTOFactory(factory.Factory):
    class Meta:
        model = PetDetailsDTO

    pet_id = 1
    name = "husky"
    pet_category = PetCategory.DOG.value
    size = PetSize.SMALL.value
    gender = PetGender.FEMALE.value
    status = PetStatus.AVAILABLE.value
    shelter_id = 1


class GetPetsFilterParamsDTOFactory(factory.Factory):
    class Meta:
        model = GetPetsFilterParamsDTO

    shelter_id = 2
    pet_category: PetCategory.CAT.value
    size = PetSize.LARGE.value
    gender = PetGender.MALE.value
