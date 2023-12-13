import pytest
import json
from freezegun import freeze_time
from datetime import datetime
from pets_core.presenters.create_adoption_request_presenter_implementation import PresenterImplementation
from pets_core.tests.factories.storage_dtos import AdoptionRequestDTOFactory


class TestCreateAdoptionRequestPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_raise_exception_for_invalid_pet(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_invalid_pet()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_PET")

    def test_raise_exception_for_pet_already_adopted(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_pet_already_adopted()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "PET_ALREADY_ADOPTED")

    def test_raise_exception_for_user_is_not_adopter(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_user_is_not_adopter()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "USER_IS_NOT_ADOPTER")

    def test_raise_exception_for_adoption_request_already_raised(self, snapshot, presenter):
        # Act
        actual_response = presenter.raise_exception_for_adoption_request_already_raised()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "ADOPTION_REQUEST_ALREADY_RAISED")


    def test_get_response_for_create_adoption_request(self, snapshot, presenter, adoption_request_dto):
        # Act
        requested_at = str(datetime(2023, 1, 1))
        adoption_request_dto = AdoptionRequestDTOFactory(requested_at=requested_at)
        actual_response = presenter.get_response_for_create_adoption_request(adoption_request_dto)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Adoption Request details response")
