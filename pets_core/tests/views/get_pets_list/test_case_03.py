"""
Test with wrong shelter, Response with 401
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.tests.factories.models import PetFactory, ShelterFactory
from pets_core.models.shelter import Shelter
import factory


class TestCase01GetPetsListAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_with_wrong_shelter(self, snapshot, create_shelters_and_pets_in_them, api_user):
        shelter2 = Shelter.objects.get(shelter_id=2)
        shelter2.user_id = str(api_user.user_id)
        shelter2.save()
        body = {}
        path_params = {"shelter_id": 1}
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
