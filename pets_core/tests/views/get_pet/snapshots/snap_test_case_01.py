# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestWithValidPetId.test_case status_code'] = '200'

snapshots['TestWithValidPetId.test_case body'] = {
    'age': 1,
    'gender': 'MALE',
    'name': 'name0',
    'pet_category': 'DOG',
    'pet_id': 1,
    'size': 'SMALL'
}
