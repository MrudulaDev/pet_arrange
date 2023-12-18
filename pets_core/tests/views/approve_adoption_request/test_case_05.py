"""
# TODO: Update test case description
"""
import pytest
from freezegun import freeze_time
from datetime import datetime
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.models.shelter import Shelter


class TestCase05ApproveAdoptionRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    @freeze_time("2023-03-15 12:30:00")
    def test_with_valid_data(self, snapshot, load_adoption_requests, api_user):
        Shelter.objects.filter(shelter_id=1).update(user_id=str(api_user.user_id))
        body = {'request_id': 1}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                       snapshot=snapshot)
