from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated, List, Dict, Any

from usecases.user.usecase import UserInputBoundary
from infrastructure.dependencies import get_usecase

router = APIRouter()

class UserController:
    def route(self):
        @router.post("/users/", response_model=Dict[str, Any])
        async def create_user_endpoint(
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)],
            name: str = Query(..., description="ユーザー名"),
            email: str = Query(..., description="メールアドレス")
        ):
            result = usecase.create_user(name, email)
            if "error" in result:
                raise HTTPException(status_code=400, detail=result["message"])
            return result

        @router.get("/users/{user_id}", response_model=Dict[str, Any])
        async def get_user_endpoint(
            user_id: int,
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)]
        ):
            result = usecase.get_user(user_id)
            if "error" in result:
                raise HTTPException(status_code=404, detail=result["message"])
            return result

        @router.get("/users/", response_model=List[Dict[str, Any]])
        async def get_all_users_endpoint(
            usecase: Annotated[UserInputBoundary, Depends(get_usecase)]
        ):
            return usecase.get_all_users()
            
        return router