from dataclasses import dataclass
from typing import Optional
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus

@dataclass
class PetDetailsDTO:
    pet_id: int
    name: str
    age: Optional[int]
    pet_category: PetCategory
    pet_size: PetSize
    gender: PetGender
    status: Optional[PetStatus]
    shelter_id: Optional[int]
@dataclass
class GetPetsFilterParamsDTO:
    shelter_id: int
    pet_category: Optional[PetCategory]
    pet_size: Optional[PetSize]
    gender: Optional[PetGender]

@dataclass
class UpdatePetDetailsDTO:
    pet_id: int
    name: str
    pet_category: PetCategory
    pet_size: PetSize
    gender: PetGender
    age: Optional[int] = 0
