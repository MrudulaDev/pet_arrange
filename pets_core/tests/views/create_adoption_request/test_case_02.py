"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.models.pet import Pet
from pets_core.constants.enums import PetStatus

class TestCase02CreateAdoptionRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_with_already_adopted_pet(self, snapshot, create_shelters_and_pets, load_adopters):
        #Arrange
        pet_id = 1
        # todo: If our objective is populating only one pet and having specific attributes for it,
        #  then it is much better to directly use PetModelFactory instead of fixtures
        Pet.objects.filter(pet_id=pet_id).update(status=PetStatus.ADOPTED.value)
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
