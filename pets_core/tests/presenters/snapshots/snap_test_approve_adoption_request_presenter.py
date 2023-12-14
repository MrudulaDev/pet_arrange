# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestApproveAdoptionRequestPresenterImplementation.test_raise_exception_for_request_not_found ADOPTION_REQUEST_NOT_FOUND'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_NOT_FOUND',
    'response': 'adoption request is not found'
}

snapshots['TestApproveAdoptionRequestPresenterImplementation.test_raise_exception_for_request_access_denied ADOPTION_REQUEST_ACCESS_DENIED'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_ACCESS_DENIED',
    'response': 'user does not have access to the adoption request'
}

snapshots['TestApproveAdoptionRequestPresenterImplementation.test_raise_exception_for_request_already_approved ADOPTION_REQUEST_ALREADY_APPROVED'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_ALREADY_APPROVED',
    'response': 'adoption request has already been approved'
}

snapshots['TestApproveAdoptionRequestPresenterImplementation.test_raise_exception_for_request_closed ADOPTION_REQUEST_CLOSED'] = {
    'http_status_code': 400,
    'res_status': 'ADOPTION_REQUEST_CLOSED',
    'response': 'adoption request has been closed'
}

snapshots['TestApproveAdoptionRequestPresenterImplementation.test_get_response_for_approve_adoption_request Adoption Request details response'] = {
    'adopter_id': 1,
    'pet_id': 1,
    'request_id': 1,
    'request_status': 'OPEN',
    'requested_at': '2023-01-01 00:00:00'
}
