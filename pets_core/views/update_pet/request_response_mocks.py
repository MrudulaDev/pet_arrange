

REQUEST_BODY_JSON = """
{
    "pet_id": 1,
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "size": "SMALL",
    "gender": "MALE"
}
"""


RESPONSE_200_JSON = """
{
    "pet_id": 1,
    "name": "string",
    "age": 1,
    "pet_category": "DOG",
    "size": "SMALL",
    "gender": "MALE"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "WRONG_PET_ID"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_PET_ID"
}
"""

