from fastapi import Depends
from typing import Annotated
import os

from config.settings import get_settings
from usecases.user.usecase import UserRepositoryInterface, UserUseCasesInteractor, UserInputBoundary, UserOutputBoundary
from infrastructure.database.user.repository import UserRepositoryImpl
from infrastructure.mock.user.repository import MockUserRepositoryImpl
from interfaces.presenters.user.presenter import UserPresenter

def get_repository() -> UserRepositoryInterface:
    """環境設定に基づいてリポジトリを提供"""
    settings = get_settings()
    
    if settings.USE_MOCK_DB:
        # 開発環境ではモックリポジトリを使用
        print(f"Using mock repository for environment: {settings.APP_ENV}")
        return MockUserRepositoryImpl()
    else:
        # テスト環境など他の環境では実際のDBリポジトリを使用
        db_url = settings.DATABASE_URL
        print(f"Using real repository with DB: {db_url} for environment: {settings.APP_ENV}")
        
        # PostgreSQLまたはSQLiteに応じて適切な方法でリポジトリを初期化
        if db_url.startswith("postgresql://"):
            # PostgreSQLに接続
            print("Connecting to PostgreSQL database")
            return UserRepositoryImpl(db_url=db_url)
        elif db_url.startswith("sqlite:///"):
            # SQLiteに接続
            db_path = db_url.split("///")[1]
            print(f"Connecting to SQLite database at {db_path}")
            return UserRepositoryImpl(db_path=db_path)
        else:
            # その他のDB接続方法
            print(f"Connecting to database with URL: {db_url}")
            return UserRepositoryImpl(db_url=db_url)

def get_presenter() -> UserOutputBoundary:
    """プレゼンターを提供"""
    return UserPresenter()

def get_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserOutputBoundary, Depends(get_presenter)]
) -> UserInputBoundary:
    """ユースケースを提供"""
    return UserUseCasesInteractor(repo, presenter) 