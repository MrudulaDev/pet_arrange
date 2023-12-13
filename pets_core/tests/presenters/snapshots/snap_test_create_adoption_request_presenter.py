# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateAdoptionRequestPresenterImplementation.test_get_response_for_create_adoption_request Adoption Request details response'] = {
    'adopter_id': 1,
    'pet_id': 1,
    'request_id': 1,
    'request_status': 'OPEN',
    'requested_at': '2023-01-01 00:00:00'
}

snapshots['TestCreateAdoptionRequestPresenterImplementation.test_raise_exception_for_invalid_pet INVALID_PET'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PET_ID',
    'response': 'Pet Does not exist'
}

snapshots['TestCreateAdoptionRequestPresenterImplementation.test_raise_exception_for_pet_already_adopted PET_ALREADY_ADOPTED'] = {
    'http_status_code': 400,
    'res_status': 'PET_ALREADY_ADOPTED',
    'response': 'pet is already adopted'
}

snapshots['TestCreateAdoptionRequestPresenterImplementation.test_raise_exception_for_user_is_not_adopter USER_IS_NOT_ADOPTER'] = {
    'http_status_code': 400,
    'res_status': 'USER_IS_NOT_ADOPTER',
    'response': 'user is not an adopter to raise an adoption request'
}

snapshots['TestCreateAdoptionRequestPresenterImplementation.test_raise_exception_for_adoption_request_already_raised ADOPTION_REQUEST_ALREADY_RAISED'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_ALREADY_RAISED',
    'response': 'adoption request is already raised'
}
