import os
import uvicorn
from fastapi import FastAPI

from interfaces.controllers.user.controller import UserController
from config.environment import env

# アプリケーション作成
app = FastAPI(title=env.APP_NAME)

# コントローラーの登録
user_controller = UserController()
app.include_router(user_controller.route(), tags=["users"])

@app.get("/", tags=["root"])
async def root():
    return {
        "message": f"{env.APP_NAME} API",
        "version": env.API_VERSION,
        "environment": os.getenv("ENV", "development"),
        "using_mock": env.USE_MOCK_DB,
        "database_url": env.DATABASE_URL
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=env.DEBUG_MODE)