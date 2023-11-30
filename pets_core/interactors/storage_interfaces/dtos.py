from dataclasses import dataclass


@dataclass
class PetDetailsDTO:
    pet_id: int
    name: str
    age: int # todo: should add the optional typing here
    pet_category: str
    size: str
    gender: str
    status: str


@dataclass
class PetIdDTO:
    pet_id: int


