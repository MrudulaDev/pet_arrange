# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetPetsListAPITestCase.test_with_valid_data status_code'] = '200'

snapshots['TestCase01GetPetsListAPITestCase.test_with_valid_data body'] = {
    'all_pets': [
        {
            'age': 1,
            'gender': 'FEMALE',
            'name': 'name0',
            'pet_category': 'DOG',
            'pet_id': 1,
            'pet_size': 'SMALL'
        }
    ]
}
