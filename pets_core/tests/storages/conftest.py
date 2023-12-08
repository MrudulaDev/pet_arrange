import pytest, factory
from pets_core.models.pet import Pet
from pets_core.models.shelter import Shelter
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus
from pets_core.tests.factories.models import PetFactory, ShelterFactory


@pytest.fixture()
def create_pet():
    pet = {
        "pet_id": 1,
        "name": "husky",
        "age": 1,
        "pet_category": PetCategory.DOG.value,
        "size": PetSize.SMALL.value,
        "gender": PetGender.FEMALE.value,
        "status": PetStatus.AVAILABLE.value
    }
    pet = Pet.objects.create(
        pet_id=pet['pet_id'],
        name=pet['name'],
        age=pet['age'],
        pet_category=pet['pet_category'],
        size=pet['size'],
        gender=pet['gender'],
        status=pet['status']
    )
    return pet


@pytest.fixture()
def create_shelters():
    shelters_details = [{
        "shelter_id": 1,
        "name": "Happy Homes",
        "user_id": "user1",
        "address": "Hyderabad"
    }, {
        "shelter_id": 2,
        "name": "Rescued Pets",
        "user_id": "user2",
        "address": "Hyderabad"
    }]
    shelters_list = []
    for shelter_detail in shelters_details:
        shelter = Shelter.objects.create(
            shelter_id=shelter_detail['shelter_id'],
            name=shelter_detail['name'],
            user_id=shelter_detail['user_id'],
            address=shelter_detail['address']
        )
        shelters_list += [shelter]
    return shelters_list


@pytest.fixture()
def create_pets():
    pets = [{
        "pet_id": 1,
        "name": "husky",
        "age": 1,
        "pet_category": PetCategory.DOG.value,
        "size": PetSize.SMALL.value,
        "gender": PetGender.FEMALE.value,
        "status": PetStatus.AVAILABLE.value,
        "shelter": 1
    },
        {
            "pet_id": 2,
            "name": "catty",
            "age": 1,
            "pet_category": PetCategory.CAT.value,
            "size": PetSize.LARGE.value,
            "gender": PetGender.MALE.value,
            "status": PetStatus.AVAILABLE.value,
            "shelter": 1
        },
        {
            "pet_id": 3,
            "name": "whitey",
            "age": 1,
            "pet_category": PetCategory.RABBIT.value,
            "size": PetSize.SMALL.value,
            "gender": PetGender.MALE.value,
            "status": PetStatus.AVAILABLE.value,
            "shelter": 2
        }
    ]
    pets_list = []
    for pet in pets:
        pet_obj = Pet.objects.create(
            pet_id=pet['pet_id'],
            name=pet['name'],
            age=pet['age'],
            pet_category=pet['pet_category'],
            size=pet['size'],
            gender=pet['gender'],
            status=pet['status']
        )
        pets_list += [pet_obj]
    return pets_list


@pytest.fixture()
def create_shelters_and_pets_in_them_return_pets_list():
    shelter_id_values = [1, 2]
    ShelterFactory.create_batch(2, shelter_id=factory.Iterator(shelter_id_values))
    shelter1 = Shelter.objects.get(shelter_id=1)
    pet_id_values = [1, 2, 3, 4, 5]
    pet_category_values = ['DOG', 'CAT', 'DOG', 'RABBIT', 'OTHERS']
    pet_size_values = ['SMALL', 'MEDIUM', 'LARGE', 'SMALL', 'MEDIUM']
    gender_values = ['FEMALE', 'MALE', 'FEMALE', 'MALE', 'FEMALE']
    PetFactory.create_batch(5, pet_id=factory.Iterator(pet_id_values),
                            pet_category=factory.Iterator(pet_category_values),
                            pet_size=factory.Iterator(pet_size_values),
                            gender=factory.Iterator(gender_values),
                            shelter=shelter1)
    pets_list = Pet.objects.all()
    return pets_list
