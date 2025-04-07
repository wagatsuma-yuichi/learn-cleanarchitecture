from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Any

from entities.user.entity import User

class UserRepositoryInterface(Protocol):
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def get_all_users(self) -> List[User]:
        raise NotImplementedError

class UserOutputBoundary(Protocol):
    def present_user(self, user: User) -> Dict[str, Any]:
        raise NotImplementedError
        
    def present_users(self, users: List[User]) -> List[Dict[str, Any]]:
        raise NotImplementedError
        
    def present_error(self, message: str) -> Dict[str, Any]:
        raise NotImplementedError

class UserInputBoundary(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_all_users(self) -> List[Dict[str, Any]]:
        raise NotImplementedError

class UserUseCasesInteractor(UserInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface, presenter: UserOutputBoundary):
        self.user_repository = user_repository
        self.presenter = presenter

    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        try:
            user = User(id=0, name=name, email=email)
            created_user = self.user_repository.create_user(user)
            return self.presenter.present_user(created_user)
        except Exception as e:
            return self.presenter.present_error(str(e))

    def get_user(self, user_id: int) -> Dict[str, Any]:
        try:
            user = self.user_repository.get_user(user_id)
            return self.presenter.present_user(user)
        except Exception as e:
            return self.presenter.present_error(str(e))

    def get_all_users(self) -> List[Dict[str, Any]]:
        try:
            users = self.user_repository.get_all_users()
            return self.presenter.present_users(users)
        except Exception as e:
            return [self.presenter.present_error(str(e))]