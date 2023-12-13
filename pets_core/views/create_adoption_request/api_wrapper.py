from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.create_adoption_request_presenter_implementation import PresenterImplementation
from pets_core.interactors.create_adoption_request_interactor import CreateAdoptionRequestInteractor
from pets_core.interactors.storage_interfaces.dtos import CreateAdoptionRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # todo: Access user_id from the attribute instead of depending on __str__ method of user class
    user_id = str(kwargs['user'])
    request_data = kwargs['request_data']
    pet_id = request_data['pet_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateAdoptionRequestInteractor(storage=storage)
    create_adoption_request_dto = CreateAdoptionRequestDTO(
        user_id=user_id,
        pet_id=pet_id
    )
    return interactor.create_adoption_request_wrapper(create_adoption_request_dto, presenter=presenter)
