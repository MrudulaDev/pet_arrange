# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04CreateAdoptionRequestAPITestCase.test_with_duplicate_request status_code'] = '400'

snapshots['TestCase04CreateAdoptionRequestAPITestCase.test_with_duplicate_request body'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_ALREADY_RAISED',
    'response': 'adoption request is already raised'
}
