from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.delete_pet_presenter_implementation import PresenterImplementation
from pets_core.interactors.delete_pet_interactor import DeletePetInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = str(user.user_id)
    pet_id = int(kwargs['pet_id'])
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeletePetInteractor(storage=storage)
    result = interactor.delete_pet_wrapper(user_id=user_id, pet_id=pet_id, presenter=presenter)
    return result
