from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.update_pet_presenter_implementation import PresenterImplementation
from pets_core.interactors.update_pet_interactor import UpdatePetInteractor
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    pet_id = kwargs['pet_id']
    request_data = kwargs['request_data']
    name = request_data['name']
    age = request_data['age']
    pet_category = request_data['pet_category']
    size = request_data['size']
    gender = request_data['gender']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdatePetInteractor(storage=storage)
    pet_details_dto = PetDetailsDTO(
        pet_id=pet_id,
        name=name,
        age=age,
        pet_category=pet_category,
        size=size,
        gender=gender
    )
    result = interactor.update_pet_wrapper(user_id=user_id, pet_details_dto=pet_details_dto, presenter=presenter)
    return result
