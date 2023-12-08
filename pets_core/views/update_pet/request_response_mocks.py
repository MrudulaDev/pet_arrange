

REQUEST_BODY_JSON = """
{
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "pet_size": "SMALL",
    "gender": "MALE"
}
"""


RESPONSE_200_JSON = """
{
    "pet_id": 1,
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "pet_size": "SMALL",
    "gender": "MALE"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "PET_NOT_FOUND_IN_SHELTER"
}
"""

