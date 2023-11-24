

REQUEST_BODY_JSON = """
{
    "shelter_id": 1,
    "name": "string",
    "address": "string",
    "phone_number": 1,
    "email": "string"
}
"""


RESPONSE_200_JSON = """
{
    "shelter_id": 1,
    "name": "string",
    "address": "string",
    "phone_number": 1,
    "email": "string"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "NAME_ALREADY_IN_USE"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_SHELTER_ID"
}
"""

