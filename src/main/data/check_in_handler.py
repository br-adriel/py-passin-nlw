from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.check_ins_repository import CheckInsRepository


class CheckInHandler:
    def __init__(self) -> None:
        self.__check_ins_repository = CheckInsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        check_in_info = http_request.param.get('attendee_id')
        self.__check_ins_repository.insert_check_in(check_in_info)
        return HttpResponse(body=None, status_code=201)
