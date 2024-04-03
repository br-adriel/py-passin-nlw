from src.models.repository.attendees_repository import AttendeesRepository


class AttendeeHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
