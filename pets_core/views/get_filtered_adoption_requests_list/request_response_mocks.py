


RESPONSE_200_JSON = """
{
    "adoption_requests": [
        {
            "request_id": 1,
            "request_status": "OPEN",
            "pet_id": 1,
            "adopter_id": 1,
            "requested_at": "2099-12-31 00:00:00"
        }
    ]
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "WRONG_SHELTER_ID"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "SHELTER_NOT_FOUND"
}
"""

