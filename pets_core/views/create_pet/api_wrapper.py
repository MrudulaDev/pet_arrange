from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.create_pet_presenter_implementation import PresenterImplementation
from pets_core.interactors.create_pet_interactor import CreatePetInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user']
    shelter_id = kwargs['shelter_id']
    pet_id = kwargs['pet_id']
    name = kwargs['name']
    age = kwargs['age']
    pet_category = kwargs['pet_category']
    size = kwargs['size']
    gender = kwargs['gender']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreatePetInteractor(storage=storage)
    return interactor.create_pet_wrapper(user_id=user_id, pet_id=pet_id, shelter_id=shelter_id, name=name, age=age,
                                         pet_category=pet_category,
                                         size=size, gender=gender, presenter=presenter)
