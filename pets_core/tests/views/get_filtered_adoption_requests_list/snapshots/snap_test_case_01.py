# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFilteredAdoptionRequestsListAPITestCase.test_with_invalid_shelter_id status_code'] = '404'

snapshots['TestCase01GetFilteredAdoptionRequestsListAPITestCase.test_with_invalid_shelter_id body'] = {
    'http_status_code': 404,
    'res_status': 'SHELTER_NOT_FOUND',
    'response': 'Shelter Not Found'
}
