from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated, List

from usecases.user.usecase import UserInputBoundary
from entities.user.entity import User
from infrastructure.dependencies import get_usecase

router = APIRouter()

class UserController:
    def route(self):
        @router.post("/users/", response_model=User)
        async def create_user_endpoint(
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)],
            name: str = Query(..., description="ユーザー名"),
            email: str = Query(..., description="メールアドレス")
        ):
            try:
                return usecase.create_user(name, email)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))

        @router.get("/users/{user_id}", response_model=User)
        async def get_user_endpoint(
            user_id: int,
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)]
        ):
            try:
                return usecase.get_user(user_id)
            except Exception as e:
                raise HTTPException(status_code=404, detail=str(e))

        @router.get("/users/", response_model=List[User])
        async def get_all_users_endpoint(
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)]
        ):
            return usecase.get_all_users()
            
        return router