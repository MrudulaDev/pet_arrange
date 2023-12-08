import pytest
import json

from pets_core.presenters.get_pet_presenter_implementation import PresenterImplementation


class TestGetPetPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_raise_exception_for_invalid_pet(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_invalid_pet()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID PET")

    def test_raise_exception_for_wrong_shelter(self, snapshot, presenter):
        # Arrange
        actual_response = presenter.raise_exception_for_wrong_shelter()
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "WRONG SHELTER")

    def test_get_response_for_get_pet(self, snapshot, presenter, pet_details_dto):
        # Arrange
        actual_response = presenter.get_response_for_get_pet(pet_details_dto)
        # Act

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Pet details response")
