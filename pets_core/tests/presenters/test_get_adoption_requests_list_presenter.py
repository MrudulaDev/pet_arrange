import pytest
import json
from datetime import datetime
from pets_core.presenters.get_adoption_requests_list_presenter_implementation import PresenterImplementation
from pets_core.tests.factories.storage_dtos import AdoptionRequestDTOFactory


class TestGetAdoptionRequestsListPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_raise_exception_for_shelter_not_found(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_shelter_not_found()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "SHELTER_NOT_FOUND")

    def test_raise_exception_for_wrong_shelter(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_wrong_shelter()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "WRONG_SHELTER_ID")

    def test_get_response_for_get_adoption_requests_list(self, snapshot, presenter):
        # Act
        requested_at = str(datetime(2023, 1, 1))
        requests_list_dto = [AdoptionRequestDTOFactory(requested_at=requested_at)]
        actual_response = presenter.get_response_for_get_adoption_requests_list(requests_list_dto)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Adoption Requests list response")
