from dataclasses import dataclass


@dataclass
class PetDetailsDTO:
    pet_id: int
    name: str
    age: int
    pet_category: str
    size: str
    gender: str
    status: str


@dataclass
class PetIdDTO:
    pet_id: int


