# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetAdoptionRequestAPITestCase.test_with_invalid_user status_code'] = '200'

snapshots['TestCase02GetAdoptionRequestAPITestCase.test_with_invalid_user body'] = {
    'adopter_id': 1,
    'pet_id': 1,
    'request_id': 0,
    'request_status': 'OPEN',
    'requested_at': '2023-12-14 16:09:15.875195'
}
