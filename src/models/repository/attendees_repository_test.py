from src.models.repository.attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


def test_insert_attendee():
    attendee = {
        "uuid": "1",
        "name": "Fulano da Silva",
        "email": "fulanosilva@gmail.com",
        "event_id": '1'
    }

    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee)
    print(response)
