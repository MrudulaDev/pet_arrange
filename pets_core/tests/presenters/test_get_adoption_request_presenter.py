import pytest
import json
from datetime import datetime
from pets_core.presenters.get_adoption_request_presenter_implementation import PresenterImplementation
from pets_core.tests.factories.storage_dtos import AdoptionRequestDTOFactory


class TestGetAdoptionRequestPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_raise_exception_for_request_not_found(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_request_not_found()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "ADOPTION_REQUEST_NOT_FOUND")

    def test_raise_exception_for_request_access_denied(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_request_access_denied()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "ADOPTION_REQUEST_ACCESS_DENIED")

    def test_get_response_for_get_adoption_request(self, snapshot, presenter):
        # Act
        requested_at = str(datetime(2023, 1, 1))
        adoption_request_dto = AdoptionRequestDTOFactory(requested_at=requested_at)
        actual_response = presenter.get_response_for_get_adoption_request(adoption_request_dto)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Adoption Request details response")
