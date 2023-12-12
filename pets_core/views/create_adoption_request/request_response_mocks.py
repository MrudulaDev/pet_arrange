

REQUEST_BODY_JSON = """
{
    "pet_id": 1
}
"""


RESPONSE_201_JSON = """
{
    "request_id": 1,
    "request_status": "OPEN",
    "pet_id": 1,
    "adopter_id": 1,
    "requested_at": "2099-12-31 00:00:00"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "PET_ALREADY_ADOPTED"
}
"""

