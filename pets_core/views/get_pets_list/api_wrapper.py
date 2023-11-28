from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.get_pets_list_presenter_implementation import GetPetsListPresenterImplementation
from pets_core.interactors.get_pets_list_interactor import GetPetsListInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    shelter_id = int(kwargs['shelter_id'])
    gender = kwargs['request_query_params']['gender']
    pet_category = kwargs['request_query_params']['pet_category']
    size = kwargs['request_query_params']['size']
    storage = StorageImplementation()
    presenter = GetPetsListPresenterImplementation()
    interactor = GetPetsListInteractor(storage=storage)
    result = interactor.get_pets_list_wrapper(user_id=user_id, shelter_id=shelter_id, gender=gender,
                                              pet_category=pet_category, size=size, presenter=presenter)
    return result
