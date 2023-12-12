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


class PetNotFound(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class PetAlreadyAdopted(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class AdoptionRequestAlreadyRaised(Exception):
    def __init__(self, request_id: int):
        self.request_id = request_id


class UserIsNotAdopter(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id


class AdoptionRequestNotFound(Exception):
    def __init__(self, request_id: int):
        self.request_id = request_id


class AdoptionRequestAccessDenied(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id


class AdoptionRequestAlreadyApproved(Exception):
    def __init__(self, request_id: int):
        self.request_id = request_id


class AdoptionRequestClosed(Exception):
    def __init__(self, request_id: int):
        self.request_id = request_id
