from dataclasses import dataclass
from typing import Optional
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus

@dataclass
class PetDetailsDTO:
    pet_id: int
    name: str
    age: Optional[int]
    pet_category: PetCategory
    size: PetSize
    gender: PetGender
    status: Optional[PetStatus]
    shelter_id: int

@dataclass
class GetPetsFilterParamsDTO:
    shelter_id: int
    pet_category: Optional[PetCategory]
    size: Optional[PetSize]
    gender: Optional[PetGender]
