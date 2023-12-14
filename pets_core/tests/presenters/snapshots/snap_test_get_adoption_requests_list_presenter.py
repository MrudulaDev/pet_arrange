# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetAdoptionRequestsListPresenterImplementation.test_raise_exception_for_shelter_not_found SHELTER_NOT_FOUND'] = {
    'http_status_code': 404,
    'res_status': 'SHELTER_NOT_FOUND',
    'response': 'Shelter Not Found'
}

snapshots['TestGetAdoptionRequestsListPresenterImplementation.test_raise_exception_for_wrong_shelter WRONG_SHELTER_ID'] = {
    'http_status_code': 401,
    'res_status': 'WRONG_SHELTER_ID',
    'response': 'User does not have access to this shelter'
}

snapshots['TestGetAdoptionRequestsListPresenterImplementation.test_get_response_for_get_adoption_requests_list Adoption Requests list response'] = {
    'adoption_requests_list': [
        {
            'adopter_id': 1,
            'pet_id': 1,
            'request_id': 1,
            'request_status': 'OPEN',
            'requested_at': '2023-01-01 00:00:00'
        }
    ]
}
