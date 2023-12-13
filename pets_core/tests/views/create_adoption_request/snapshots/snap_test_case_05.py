# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05CreateAdoptionRequestAPITestCase.test_with_valid_data status_code'] = '201'

snapshots['TestCase05CreateAdoptionRequestAPITestCase.test_with_valid_data body'] = {
    'adopter_id': 1,
    'pet_id': 1,
    'request_id': 1,
    'request_status': 'OPEN',
    'requested_at': '2023-12-13 16:21:06.877865'
}
