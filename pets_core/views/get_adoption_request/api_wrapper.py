from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.get_adoption_request_presenter_implementation import PresenterImplementation
from pets_core.interactors.get_adoption_request_interactor import GetAdoptionRequestInteractor
from pets_core.interactors.storage_interfaces.dtos import GetAdoptionRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    request_data = kwargs['request_data']
    request_id = request_data['request_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAdoptionRequestInteractor(storage=storage)
    get_adoption_request_dto = GetAdoptionRequestDTO(user_id=user_id, request_id=request_id)
    return interactor.get_adoption_request_wrapper(get_adoption_request_dto, presenter=presenter)
