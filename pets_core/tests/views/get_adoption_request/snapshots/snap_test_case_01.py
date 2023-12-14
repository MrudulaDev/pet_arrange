# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdoptionRequestAPITestCase.test_with_invalid_request_id status_code'] = '400'

snapshots['TestCase01GetAdoptionRequestAPITestCase.test_with_invalid_request_id body'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_NOT_FOUND',
    'response': 'adoption request is not found'
}
