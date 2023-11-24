from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    try:
        from pets_core.views.shelter_filtered_pets.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'shelter_id': 382},
        "query_params": {'type': 'Dog', 'size': 'small', 'gender': 'male'},
        "header_params": {},
        "body": body,
        "securities": [{'oauth': ['superuser']}]
    }

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        response = ''
        status_code = 200
        if '200' in ['200', '401']:
            from pets_core.views.shelter_filtered_pets.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '401']:
            from pets_core.views.shelter_filtered_pets.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="pets_core", test_case=test_case,
        operation_name="shelter_filtered_pets",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple