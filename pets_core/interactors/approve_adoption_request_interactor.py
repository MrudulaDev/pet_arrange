from pets_core.interactors.presenter_interfaces.approve_adoption_request_presenter_interface import \
    ApproveAdoptionRequestPresenterInterface
from pets_core.interactors.storage_interfaces.storage_interface import StorageInterface
from pets_core.exceptions.custom_exceptions import AdoptionRequestNotFound, AdoptionRequestAccessDenied, \
    AdoptionRequestAlreadyApproved, AdoptionRequestClosed
from django.http import HttpResponse
from pets_core.interactors.storage_interfaces.dtos import AdoptionRequestDTO, ApproveAdoptionRequestDTO


class ApproveAdoptionRequestInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def approve_adoption_request_wrapper(self, approve_adoption_request_dto: ApproveAdoptionRequestDTO,
                                         presenter: ApproveAdoptionRequestPresenterInterface) -> HttpResponse:
        try:
            adoption_request_dto = self.approve_adoption_request(
                approve_adoption_request_dto=approve_adoption_request_dto)
        except AdoptionRequestNotFound:
            return presenter.raise_exception_for_request_not_found()
        except AdoptionRequestAccessDenied:
            return presenter.raise_exception_for_request_access_denied()
        except AdoptionRequestAlreadyApproved:
            return presenter.raise_exception_for_request_already_approved()
        except AdoptionRequestClosed:
            return presenter.raise_exception_for_request_closed()
        return presenter.get_response_for_approve_adoption_request(adoption_request_dto=adoption_request_dto)

    def approve_adoption_request(self, approve_adoption_request_dto) -> AdoptionRequestDTO:
        # todo: typing for input args
        self.storage.validate_adoption_request_id(request_id=approve_adoption_request_dto.request_id)
        self.storage.validate_adoption_request_access(request_id=approve_adoption_request_dto.request_id,
                                                      user_id=approve_adoption_request_dto.user_id)
        # todo: instead of doing the below two validations in a separate storage method (hits database twice),
        #  we can fetch the request status (hits database once) and validate below validations in interactor
        self.storage.validate_adoption_request_already_approved(request_id=approve_adoption_request_dto.request_id)
        self.storage.validate_adoption_request_closed(request_id=approve_adoption_request_dto.request_id)
        adoption_request_dto = self.storage.approve_adoption_request(
            approve_adoption_request_dto=approve_adoption_request_dto)
        self.storage.close_all_other_adoption_requests_on_requested_pet(request_id=approve_adoption_request_dto.request_id)
        return adoption_request_dto
