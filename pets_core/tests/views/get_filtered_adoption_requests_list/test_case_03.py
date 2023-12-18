"""
# TODO: Update test case description
"""
import pytest
from freezegun import freeze_time
from datetime import datetime
from pets_core.models.request import Request
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.models.shelter import Shelter


class TestCase02GetFilteredAdoptionRequestsListAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_valid_data(self, snapshot, load_adoption_requests, api_user):
        Shelter.objects.filter(shelter_id=1).update(user_id=api_user.user_id)
        Request.objects.update(requested_at=datetime.now())
        body = {}
        path_params = {"shelter_id": 1}
        query_params = {'name': "", 'pet_category': ''}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
