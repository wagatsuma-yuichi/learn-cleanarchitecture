from fastapi import APIRouter

from usecases.user.usecase import UserInputBoundary, User

router = APIRouter()

class UserController:
    def __init__(self, user_usecase: UserInputBoundary):
        self.user_usecase = user_usecase

    async def create_user(self, name: str, email: str) -> User:
        return self.user_usecase.create_user(name, email)

    async def get_user(self, user_id: int) -> User:
        return self.user_usecase.get_user(user_id)

    async def get_all_users(self) -> list[User]:
        return self.user_usecase.get_all_users()

    def route(self):
        @router.post("/users/")
        async def create_user_endpoint(name: str, email: str):
            return await self.create_user(name, email)

        @router.get("/users/")
        async def get_all_users_endpoint():
            return await self.get_all_users()
        return router