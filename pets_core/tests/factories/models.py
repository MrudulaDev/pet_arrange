import factory

from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter


class ShelterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shelter

    shelter_id = factory.sequence(lambda n: f"{n}")
    name = factory.sequence(lambda n: f"name{n}")
    user_id = factory.sequence(lambda n: f"name{n}")
    address = "Hyderabad"


class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    pet_id = factory.sequence(lambda n: f"{n}")
    name = factory.sequence(lambda n: f"name{n}")
    age = 1
    pet_category = factory.Iterator([pet_category.value for pet_category in PetCategory])
    pet_size = factory.Iterator([size.value for size in PetSize])
    gender = factory.Iterator([gender.value for gender in PetGender])
    status = factory.Iterator([status.value for status in PetStatus])
    shelter = factory.SubFactory(ShelterFactory)
