# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetFilteredAdoptionRequestsListAPITestCase.test_with_wrong_shelter_id status_code'] = '401'

snapshots['TestCase02GetFilteredAdoptionRequestsListAPITestCase.test_with_wrong_shelter_id body'] = {
    'http_status_code': 401,
    'res_status': 'WRONG_SHELTER_ID',
    'response': 'User does not have access to this shelter'
}
