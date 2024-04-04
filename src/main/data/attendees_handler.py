import uuid

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository


class AttendeeHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        event_id = http_request.param.get('event_id')
        event_atendees_count = self.__events_repository.count_event_attendees(
            event_id
        )
        event = self.__events_repository.get_event_by_id(event_id)

        if event_atendees_count >= event.maximum_attendees:
            raise Exception('Evento lotado')

        body['uuid'] = str(uuid.uuid4())
        body['event_id'] = event_id

        self.__attendees_repository.insert_attendee(body)
        return HttpResponse(body=None, status_code=201)
