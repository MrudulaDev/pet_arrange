from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from pets_core.storages.storage_implementation import StorageImplementation
from pets_core.presenters.create_pet_presenter_implementation import PresenterImplementation
from pets_core.interactors.create_pet_interactor import CreatePetInteractor
from pets_core.interactors.storage_interfaces.dtos import PetDetailsDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'])
    request_data = kwargs['request_data']
    shelter_id = request_data['shelter_id']
    pet_id = request_data['pet_id']
    name = request_data['name']
    pet_category = request_data['pet_category']
    size = request_data['size']
    gender = request_data['gender']
    if 'age' in request_data:
        age = request_data['age']
    else:
        age = None
    if 'status' in request_data:
        status = request_data['status']
    else:
        status = None
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreatePetInteractor(storage=storage)
    pet_details_dto = PetDetailsDTO(
        pet_id=pet_id,
        name=name,
        age=age,
        pet_category=pet_category,
        size=size,
        gender=gender,
        status=status,
        shelter_id=shelter_id
    )
    return interactor.create_pet_wrapper(user_id=user_id, pet_details_dto=pet_details_dto,
                                         presenter=presenter)
