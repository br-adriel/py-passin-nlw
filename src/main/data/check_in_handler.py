from src.models.repository.check_ins_repository import CheckInsRepository


class CheckInHandler:
    def __init__(self) -> None:
        self.__check_ins_repository = CheckInsRepository()
