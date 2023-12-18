# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02ApproveAdoptionRequestAPITestCase.test_with_closed_request status_code'] = '400'

snapshots['TestCase02ApproveAdoptionRequestAPITestCase.test_with_closed_request body'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_CLOSED',
    'response': 'adoption request has been closed'
}
