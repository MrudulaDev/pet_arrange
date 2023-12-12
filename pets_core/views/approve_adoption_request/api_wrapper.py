from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.approve_adoption_request_presenter_implementation import PresenterImplementation
from pets_core.interactors.approve_adoption_request_interactor import ApproveAdoptionRequestInteractor
from pets_core.interactors.storage_interfaces.dtos import ApproveAdoptionRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    request_data = kwargs['request_data']
    request_id = request_data['request_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = ApproveAdoptionRequestInteractor(storage=storage)
    approve_adoption_request_dto = ApproveAdoptionRequestDTO(user_id=user_id, request_id=request_id)
    return interactor.approve_adoption_request_wrapper(approve_adoption_request_dto, presenter=presenter)
