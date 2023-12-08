# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetPetPresenterImplementation.test_raise_exception_for_invalid_pet INVALID PET'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_PET_ID',
    'response': 'Pet Does not exist'
}

snapshots['TestGetPetPresenterImplementation.test_raise_exception_for_wrong_shelter WRONG SHELTER'] = {
    'http_status_code': 401,
    'res_status': 'WRONG_SHELTER_ID',
    'response': 'This shelter ID is invalid'
}

snapshots['TestGetPetPresenterImplementation.test_get_response_for_get_pet Pet details response'] = {
    'age': 1,
    'gender': 'FEMALE',
    'name': 'husky',
    'pet_category': 'DOG',
    'pet_id': 1,
    'size': 'SMALL',
    'status': 'AVAILABLE'
}
