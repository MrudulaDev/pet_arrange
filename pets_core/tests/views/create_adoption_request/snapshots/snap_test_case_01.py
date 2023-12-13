# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateAdoptionRequestAPITestCase.test_with_invalid_pet_id status_code'] = '500'

snapshots['TestCase01CreateAdoptionRequestAPITestCase.test_with_invalid_pet_id body'] = {
    'res_status': [
        '"INVALID_PET_ID" is not a valid choice.'
    ]
}
