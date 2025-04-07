from abc import ABC, abstractmethod
from typing import Protocol, List

from entities.user import User

class UserRepositoryInterface(Protocol):
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def get_all_users(self) -> List[User]:
        raise NotImplementedError

class UserInputBoundary(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_all_users(self) -> List[User]:
        raise NotImplementedError

class UserUseCasesInteractor(UserInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, name: str, email: str) -> User:
        user = User(id=0, name=name, email=email)
        return self.user_repository.create_user(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id)

    def get_all_users(self) -> List[User]:
        return self.user_repository.get_all_users()