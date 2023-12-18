from datetime import datetime

import factory

from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus, RequestStatus
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter
from pets_core.models.adopter import Adopter
from pets_core.models.request import Request


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

class AdopterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Adopter

    user_id = factory.sequence(lambda n: f"{n}")
    name = "Ram"
    preferred_pet_category = factory.Iterator([pet_category.value for pet_category in PetCategory])
    preferred_pet_size = factory.Iterator([size.value for size in PetSize])
    preferred_pet_gender = factory.Iterator([gender.value for gender in PetGender])


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Request

    request_id = factory.sequence(lambda n: f"{n}")
    request_status = RequestStatus.OPEN.value
    requested_by = factory.SubFactory(AdopterFactory)
    requested_pet = factory.SubFactory(PetFactory)
    requested_at = str(datetime.now())
    status_change_timestamp = None


