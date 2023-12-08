# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestWithWrongShelter.test_case status_code'] = '401'

snapshots['TestWithWrongShelter.test_case body'] = {
    'http_status_code': 401,
    'res_status': 'WRONG_SHELTER_ID',
    'response': 'This shelter ID is invalid'
}
