# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetFilteredAdoptionRequestsListAPITestCase.test_with_valid_data status_code'] = '200'

snapshots['TestCase02GetFilteredAdoptionRequestsListAPITestCase.test_with_valid_data body'] = {
    'adoption_requests': [
        {
            'adopter_id': 1,
            'pet_id': 1,
            'request_id': 0,
            'request_status': 'OPEN',
            'requested_at': '2023-03-15 12:30:00'
        },
        {
            'adopter_id': 2,
            'pet_id': 1,
            'request_id': 1,
            'request_status': 'OPEN',
            'requested_at': '2023-03-15 12:30:00'
        }
    ]
}
