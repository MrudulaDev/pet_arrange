# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPetsListAPITestCase.test_with_wrong_shelter status_code'] = '401'

snapshots['TestCase01GetPetsListAPITestCase.test_with_wrong_shelter body'] = {
    'http_status_code': 401,
    'res_status': 'WRONG_SHELTER_ID',
    'response': 'This shelter ID is invalid'
}
