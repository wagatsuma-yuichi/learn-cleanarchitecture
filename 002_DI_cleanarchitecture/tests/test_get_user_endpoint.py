import pytest
from fastapi import APIRouter, status, FastAPI
from fastapi.testclient import TestClient
from entities.user.entity import User
from usecases.user.data import UserGetOutputData, ErrorOutputData
from interfaces.presenters.user.http_response_presenter import HttpResponseUserGetPresenter
from interfaces.views.http_response_view import HttpResponseView

# テスト用のFastAPIアプリを作成
@pytest.fixture
def test_app():
    app = FastAPI()
    app.include_router(create_test_router())
    return app

# テストクライアント
@pytest.fixture
def test_client(test_app):
    return TestClient(test_app)


# テスト用の簡易ルーターを作成
def create_test_router():
    router = APIRouter()
    
    # 成功パターン用のモックエンドポイント
    @router.get("/users/1")
    async def get_user_success_endpoint():
        user = User(id=1, name="テストユーザー1", email="user1@example.com")
        presenter = HttpResponseUserGetPresenter()
        presenter.output(UserGetOutputData(user))
        view_model = presenter.get_view_model()
        return HttpResponseView.render(view_model)
    
    # 失敗パターン用のモックエンドポイント
    @router.get("/users/999")
    async def get_user_not_found_endpoint():
        presenter = HttpResponseUserGetPresenter()
        presenter.output_error(ErrorOutputData("User not found", status_code=404))
        view_model = presenter.get_view_model()
        return HttpResponseView.render_error(view_model)
    
    return router


@pytest.mark.asyncio
async def test_get_user_success(test_client):
    # APIエンドポイントの呼び出し
    response = test_client.get("/users/1")
    
    # アサーション
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "name": "テストユーザー1",
        "email": "user1@example.com",
        "display_name": "テストユーザー1さん"
    }

@pytest.mark.asyncio
async def test_get_user_not_found(test_client):
    # APIエンドポイントの呼び出し - 存在しないID
    response = test_client.get("/users/999")
    
    # アサーション
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "error" in response.json()
    assert response.json()["message"] == "User not found"
