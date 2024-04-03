from typing import Dict

from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.settings.connection import db_connection_handler


class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendee = Attendees(
                    id=attendee_info.get('uuid'),
                    name=attendee_info.get('name'),
                    email=attendee_info.get('email'),
                    event_id=attendee_info.get('event_id'),
                )

                database.session.add(attendee)
                database.session.commit()

                return attendee_info
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str):
        with db_connection_handler as database:
            attendee = (
                database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id == attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        ).one_or_none()
            )
            return attendee
