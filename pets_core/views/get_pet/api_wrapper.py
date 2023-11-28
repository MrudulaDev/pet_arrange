from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.get_pet_presenter_implementation import PresenterImplementation
from pets_core.interactors.get_pet_interactor import GetPetInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user']
    pet_id = int(kwargs['pet_id'])
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetPetInteractor(storage=storage)
    result = interactor.get_pet_wrapper(user_id=user_id, pet_id=pet_id, presenter=presenter)
    return result
