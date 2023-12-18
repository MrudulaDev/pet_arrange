"""
# TODO: Update test case description
"""
import pytest
import datetime
from freezegun import freeze_time
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from pets_core.models.request import Request
from pets_core.models.adopter import Adopter
from pets_core.models.shelter import Shelter
from pets_core.constants.enums import RequestStatus


class TestCase02ApproveAdoptionRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    @freeze_time('2023-03-15 12:30:00')
    def test_with_closed_request(self, snapshot, load_adoption_requests, api_user):
        request_id = 0
        Shelter.objects.filter(shelter_id=1).update(user_id=str(api_user.user_id))
        Request.objects.filter(request_id=request_id).update(request_status=RequestStatus.CLOSED.value)
        Request.objects.filter(request_id=request_id).update(requested_at=datetime.datetime.now())
        body = {'request_id': request_id}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
