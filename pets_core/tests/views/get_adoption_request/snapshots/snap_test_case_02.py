# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetAdoptionRequestAPITestCase.test_with_invalid_user status_code'] = '400'

snapshots['TestCase02GetAdoptionRequestAPITestCase.test_with_invalid_user body'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_ACCESS_DENIED',
    'response': 'user does not have access to the adoption request'
}
