"""
Test with invalid shelter_id, Response with 404
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.tests.factories.models import PetFactory, ShelterFactory
from pets_core.models.shelter import Shelter
import factory


class TestCase02GetPetsListAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_with_invalid_shelter_id(self, snapshot, create_shelters_and_pets_in_them, api_user):
        body = {}
        path_params = {"shelter_id": 3}
        query_params = {
            'pet_category': 'DOG',
            'pet_size': 'SMALL',
            'gender': 'FEMALE'
        }
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
