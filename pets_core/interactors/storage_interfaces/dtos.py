from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from pets_core.constants.enums import PetCategory, PetSize, PetGender, PetStatus, RequestStatus


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


@dataclass
class CreateAdoptionRequestDTO:
    user_id: str
    pet_id: int


@dataclass
class AdoptionRequestDTO:
    request_id: int
    request_status: RequestStatus
    pet_id: int
    adopter_id: int
    requested_at: datetime


@dataclass
class GetAdoptionRequestDTO:
    user_id: str
    request_id: int


@dataclass
class ApproveAdoptionRequestDTO:
    user_id: str
    request_id: int


@dataclass
class GetAdoptionRequestsListDTO:
    user_id: str
    shelter_id: int
    pet_name: str
    pet_category: PetCategory
