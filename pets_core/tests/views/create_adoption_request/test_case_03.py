"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.models.shelter import Shelter

class TestCase03CreateAdoptionRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_with_user_that_is_not_an_adopter(self, snapshot, api_user, create_shelters_and_pets, load_adopters):
        #Arrange
        pet_id = 1
        Shelter.objects.filter(shelter_id=1).update(user_id=str(api_user.user_id))
        body = {'pet_id': pet_id}
        path_params = {}
        query_params = {}
        headers = {}

        #Act
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
