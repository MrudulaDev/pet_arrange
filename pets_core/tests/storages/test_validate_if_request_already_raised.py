import pytest
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.exceptions.custom_exceptions import AdoptionRequestAlreadyRaised
from pets_core.models.adopter import Adopter
from pets_core.models.request import Request


class TestValidateRequestAlreadyRaised:
    @pytest.mark.django_db
    def test_when_request_not_raised(self, create_shelters_and_pets, load_adopters):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'
        adopter_id = Adopter.objects.filter(user_id=user_id).values_list('id', flat=True).first()
        pet_id = 1

        # Act
        storage.validate_if_request_already_raised(pet_id=pet_id, adopter_id=adopter_id)

    @pytest.mark.django_db
    def test_when_request_is_already_raised(self, load_adoption_requests):
        # Arrange
        storage = StorageImplementation()
        user_id = 'user1'
        adopter_id = Adopter.objects.filter(user_id=user_id).values_list('id', flat=True).first()
        pet_id = 1
        request_id = Request.objects.filter(requested_by__id=adopter_id, requested_pet__pet_id=pet_id).values_list(
            'request_id',
            flat=True).first()

        # Act
        with pytest.raises(AdoptionRequestAlreadyRaised) as err:
            storage.validate_if_request_already_raised(pet_id=pet_id, adopter_id=adopter_id)

        # Assert
        assert err.value.request_id == request_id
