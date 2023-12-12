from enum import Enum


class PetCategory(Enum):
    DOG = "DOG"
    CAT = "CAT"
    PARROT = "PARROT"
    RABBIT = "RABBIT"
    OTHERS = "OTHERS"


class PetSize(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class PetGender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class PetStatus(Enum):
    AVAILABLE = "AVAILABLE"
    ADOPTED = "ADOPTED"


class RequestStatus(Enum):
    OPEN = "OPEN"
    APPROVED = "APPROVED"
    CLOSED = "CLOSED"


class StatusCode(Enum):
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    NOT_FOUND = 404
    FORBIDDEN = 403
    SUCCESS = 200
    SUCCESS_CREATE = 201
    SUCCESS_DELETE = 204
