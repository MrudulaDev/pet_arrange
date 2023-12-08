# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPetsListAPITestCase.test_with_valid_data status_code'] = '404'

snapshots['TestCase01GetPetsListAPITestCase.test_with_valid_data body'] = {
    'http_status_code': 404,
    'res_status': 'SHELTER_NOT_FOUND',
    'response': 'Shelter Not Found'
}
