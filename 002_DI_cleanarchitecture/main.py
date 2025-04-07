import os
import uvicorn
from fastapi import FastAPI

from interfaces.controllers.user.controller import UserController
from config.settings import get_settings

# 環境設定
os.environ.setdefault("APP_ENV", "development")

# アプリケーション作成
app = FastAPI(title="Clean Architecture DI Demo")

# コントローラーの登録
user_controller = UserController()
app.include_router(user_controller.route(), tags=["users"])

@app.get("/", tags=["root"])
async def root():
    settings = get_settings()
    return {
        "message": "Clean Architecture with DI Demo",
        "environment": settings.APP_ENV,
        "using_mock": settings.USE_MOCK_DB,
        "database_url": settings.DATABASE_URL
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)