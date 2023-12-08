"""
Test with valid pet_id, Response with 200
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from pets_core.tests.factories.models import PetFactory, ShelterFactory
from pets_core.models.pet import Pet
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestWithValidPetId(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, api_user):
        # Arrange
        PetFactory(pet_id=1)
        shelter1= ShelterFactory(shelter_id=1, user_id=str(api_user.user_id))
        Pet.objects.filter(pet_id=1).update(shelter=shelter1)
        body = {}
        path_params = {"pet_id": 1}
        query_params = {}
        headers = {}

        # Act
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
