# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05ApproveAdoptionRequestAPITestCase.test_with_valid_data status_code'] = '200'

snapshots['TestCase05ApproveAdoptionRequestAPITestCase.test_with_valid_data body'] = {
    'adopter_id': 2,
    'pet_id': 1,
    'request_id': 1,
    'request_status': 'APPROVED',
    'requested_at': '2023-12-14 18:35:03.179782'
}
