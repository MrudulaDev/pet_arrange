

REQUEST_BODY_JSON = """
{
    "shelter_id": 1,
    "pet_id": 1,
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "pet_size": "SMALL",
    "gender": "MALE",
    "status": "AVAILABLE"
}
"""


RESPONSE_201_JSON = """
{
    "pet_id": 1,
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "pet_size": "SMALL",
    "gender": "MALE"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "WRONG_SHELTER_ID"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "PET_ID_ALREADY_EXISTS"
}
"""

