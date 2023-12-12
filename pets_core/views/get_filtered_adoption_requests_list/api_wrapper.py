from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.get_adoption_requests_list_presenter_implementation import PresenterImplementation
from pets_core.interactors.get_adoption_requests_list_interactor import \
    GetAdoptionRequestsListInteractor
from pets_core.interactors.storage_interfaces.dtos import GetAdoptionRequestsListDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    shelter_id = int(kwargs['shelter_id'])
    query_params = kwargs['request_query_params']
    pet_name = query_params['name']
    pet_category = query_params['pet_category']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAdoptionRequestsListInteractor(storage=storage)
    get_adoption_requests_list_dto = GetAdoptionRequestsListDTO(
        user_id=user_id,
        shelter_id=shelter_id,
        pet_name=pet_name,
        pet_category=pet_category
    )
    result = interactor.get_adoption_requests_list_wrapper(
        get_adoption_requests_list_dto=get_adoption_requests_list_dto,
        presenter=presenter)
    return result
