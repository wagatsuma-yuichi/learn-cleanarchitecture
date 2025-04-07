from fastapi import APIRouter, Depends, Query
from typing import Annotated

from usecases.user.usecase import (
    UserAddInputBoundary, UserGetInputBoundary, UserGetAllInputBoundary
)
from usecases.user.data import UserAddInputData, UserGetInputData, UserGetAllInputData
from infrastructure.dependencies import (
    get_user_add_usecase, get_user_get_usecase, get_user_get_all_usecase,
    get_user_add_presenter, get_user_get_presenter, get_user_get_all_presenter
)
from interfaces.presenters.user.http_response_presenter import (
    HttpResponseUserAddPresenter, HttpResponseUserGetPresenter, HttpResponseUserGetAllPresenter
)
from interfaces.views.http_response_view import HttpResponseView

router = APIRouter()

class UserController:
    def route(self):
        @router.post("/users/")
        async def create_user_endpoint(
            usecase: Annotated[UserAddInputBoundary, Depends(get_user_add_usecase)],
            presenter: Annotated[HttpResponseUserAddPresenter, Depends(get_user_add_presenter)],
            name: str = Query(..., description="ユーザー名"),
            email: str = Query(..., description="メールアドレス")
        ):
            input_data = UserAddInputData(name=name, email=email)
            usecase.handle(input_data)
            view_model = presenter.get_view_model()
            
            # エラーチェック
            if "error" in view_model.get_body():
                return HttpResponseView.render(view_model)
            
            # 正常応答
            return HttpResponseView.render(view_model)

        @router.get("/users/{user_id}")
        async def get_user_endpoint(
            user_id: int,
            usecase: Annotated[UserGetInputBoundary, Depends(get_user_get_usecase)],
            presenter: Annotated[HttpResponseUserGetPresenter, Depends(get_user_get_presenter)]
        ):
            input_data = UserGetInputData(user_id=user_id)
            usecase.handle(input_data)
            view_model = presenter.get_view_model()
            
            # エラーチェック
            if "error" in view_model.get_body():
                return HttpResponseView.render(view_model)
            
            # 正常応答
            return HttpResponseView.render(view_model)

        @router.get("/users/")
        async def get_all_users_endpoint(
            usecase: Annotated[UserGetAllInputBoundary, Depends(get_user_get_all_usecase)],
            presenter: Annotated[HttpResponseUserGetAllPresenter, Depends(get_user_get_all_presenter)]
        ):
            input_data = UserGetAllInputData()
            usecase.handle(input_data)
            view_model = presenter.get_view_model()
            
            # FastAPIはJSONのシリアライズを自動的に行うため、
            # 単純な辞書やリストを返す場合はrender_jsonメソッドを使用
            return HttpResponseView.render_users_json(view_model)
            
        return router