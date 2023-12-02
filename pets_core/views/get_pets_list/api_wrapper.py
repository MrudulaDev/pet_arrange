from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.get_pets_list_presenter_implementation import GetPetsListPresenterImplementation
from pets_core.interactors.get_pets_list_interactor import GetPetsListInteractor
from pets_core.interactors.storage_interfaces.dtos import GetPetsFilterParamsDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    shelter_id = int(kwargs['shelter_id'])
    query_params = kwargs['request_query_params']
    gender = query_params['gender']
    pet_category = query_params['pet_category']
    size = query_params['size']
    storage = StorageImplementation()
    presenter = GetPetsListPresenterImplementation()
    interactor = GetPetsListInteractor(storage=storage)
    get_pet_filter_params = GetPetsFilterParamsDTO(
        shelter_id=shelter_id,
        gender=gender,
        pet_category=pet_category,
        size=size
    )
    result = interactor.get_pets_list_wrapper(user_id=user_id, filter_params=get_pet_filter_params, presenter=presenter)
    return result
