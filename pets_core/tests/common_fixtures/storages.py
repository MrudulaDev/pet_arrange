import pytest
from pets_core.models.pet import Pet, Shelter
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus

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
