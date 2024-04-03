from src.models.repository.events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


def test_insert_event():
    event = {
        "uuid": "1",
        "title": "Evento 1",
        "maximum_attendees": 50,
        "slug": "meu-slug",
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


def test_get_event_by_id():
    event_id = '1'

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
