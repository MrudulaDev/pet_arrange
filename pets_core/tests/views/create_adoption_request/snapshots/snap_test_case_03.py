# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreateAdoptionRequestAPITestCase.test_with_user_that_is_not_an_adopter status_code'] = '400'

snapshots['TestCase02CreateAdoptionRequestAPITestCase.test_with_user_that_is_not_an_adopter body'] = {
    'http_status_code': 400,
    'res_status': 'USER_IS_NOT_ADOPTER',
    'response': 'user is not an adopter to raise an adoption request'
}
