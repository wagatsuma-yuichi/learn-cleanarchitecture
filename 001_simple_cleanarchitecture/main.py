from fastapi import FastAPI

from interfaces.controllers.user_controller import UserController
from usecases.user_usecase import UserUseCasesInteractor
from infrastructure.database.user_repository_impl import UserRepositoryImpl

app = FastAPI()

user_repository = UserRepositoryImpl(db_path="users.db")
user_usecase = UserUseCasesInteractor(user_repository)
user_controller = UserController(user_usecase)

app.include_router(user_controller.route())