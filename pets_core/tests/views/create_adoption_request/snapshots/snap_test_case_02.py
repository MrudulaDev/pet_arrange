# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateAdoptionRequestAPITestCase.test_with_already_adopted_pet status_code'] = '400'

snapshots['TestCase02CreateAdoptionRequestAPITestCase.test_with_already_adopted_pet body'] = {
    'http_status_code': 400,
    'res_status': 'PET_ALREADY_ADOPTED',
    'response': 'pet is already adopted'
}
