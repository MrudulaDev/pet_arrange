

class InvalidPetId(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id


class WrongShelterId(Exception):
    def __init__(self, shelter_id: int):
        self.shelter_id = shelter_id


class InvalidShelterId(Exception):
    def __init__(self, shelter_id: int):
        self.shelter_id = shelter_id


class PetIdAlreadyExists(Exception):
    def __init__(self, pet_id: int):
        self.pet_id = pet_id
