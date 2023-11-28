class InvalidPetId(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class WrongShelterId(Exception):
    def __init__(self, shelter_id: int):
        self.shelter_id = shelter_id


class InvalidAge(Exception):
    def __init__(self, age: int):
        self.age = age


class ShelterNotFound(Exception):
    def __init__(self, shelter_id: int):
        self.shelter_id = shelter_id


class PetIdAlreadyExists(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class PetNotFoundInShelter(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class NameAlreadyExists(Exception):
    def __init__(self, name: str):
        self.name = name
