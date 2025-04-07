from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Any

from entities.user.entity import User
from usecases.user.data import (
    UserAddInputData, UserAddOutputData, 
    UserGetInputData, UserGetOutputData,
    UserGetAllInputData, UserGetAllOutputData,
    ErrorOutputData, UserDeleteInputData, UserDeleteOutputData
)

class UserRepositoryInterface(Protocol):
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def get_all_users(self) -> List[User]:
        raise NotImplementedError
    
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError

class UserAddOutputBoundary(Protocol):
    def output(self, output_data: UserAddOutputData) -> None:
        raise NotImplementedError
        
    def output_error(self, output_data: ErrorOutputData) -> None:
        raise NotImplementedError

class UserGetOutputBoundary(Protocol):
    def output(self, output_data: UserGetOutputData) -> None:
        raise NotImplementedError
        
    def output_error(self, output_data: ErrorOutputData) -> None:
        raise NotImplementedError

class UserGetAllOutputBoundary(Protocol):
    def output(self, output_data: UserGetAllOutputData) -> None:
        raise NotImplementedError
        
    def output_error(self, output_data: ErrorOutputData) -> None:
        raise NotImplementedError

class UserAddInputBoundary(ABC):
    @abstractmethod
    def handle(self, input_data: UserAddInputData) -> None:
        raise NotImplementedError

class UserGetInputBoundary(ABC):
    @abstractmethod
    def handle(self, input_data: UserGetInputData) -> None:
        raise NotImplementedError

class UserGetAllInputBoundary(ABC):
    @abstractmethod
    def handle(self, input_data: UserGetAllInputData) -> None:
        raise NotImplementedError

class UserDeleteInputBoundary(ABC):
    @abstractmethod
    def handle(self, input_data: UserDeleteInputData) -> None:
        raise NotImplementedError
    
class UserDeleteOutputBoundary(Protocol):
    def output(self, output_data: UserDeleteOutputData) -> None:
        raise NotImplementedError
        
    def output_error(self, output_data: ErrorOutputData) -> None:
        raise NotImplementedError

class UserAddInteractor(UserAddInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface, presenter: UserAddOutputBoundary):
        self.user_repository = user_repository
        self.presenter = presenter

    def handle(self, input_data: UserAddInputData) -> None:
        try:
            user = User(id=0, name=input_data.name, email=input_data.email)
            created_user = self.user_repository.create_user(user)
            output_data = UserAddOutputData(created_user)
            self.presenter.output(output_data)
        except Exception as e:
            error_output = ErrorOutputData(str(e))
            self.presenter.output_error(error_output)

class UserGetInteractor(UserGetInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface, presenter: UserGetOutputBoundary):
        self.user_repository = user_repository
        self.presenter = presenter

    def handle(self, input_data: UserGetInputData) -> None:
        try:
            user = self.user_repository.get_user(input_data.user_id)
            output_data = UserGetOutputData(user)
            self.presenter.output(output_data)
        except Exception as e:
            error_output = ErrorOutputData(str(e))
            self.presenter.output_error(error_output)

class UserGetAllInteractor(UserGetAllInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface, presenter: UserGetAllOutputBoundary):
        self.user_repository = user_repository
        self.presenter = presenter

    def handle(self, input_data: UserGetAllInputData) -> None:
        try:
            users = self.user_repository.get_all_users()
            output_data = UserGetAllOutputData(users)
            self.presenter.output(output_data)
        except Exception as e:
            error_output = ErrorOutputData(str(e))
            self.presenter.output_error(error_output)

class UserDeleteInteractor(UserDeleteInputBoundary):
    def __init__(self, user_repository: UserRepositoryInterface, presenter: UserDeleteOutputBoundary):
        self.user_repository = user_repository
        self.presenter = presenter

    def handle(self, input_data: UserDeleteInputData) -> None:
        try:
            users = self.user_repository.delete_user(input_data.user_id)
            output_data = UserDeleteOutputData(users)
            self.presenter.output(output_data)
        except Exception as e:
            error_output = ErrorOutputData(str(e))
            self.presenter.output_error(error_output)