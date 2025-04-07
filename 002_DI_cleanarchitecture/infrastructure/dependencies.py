from fastapi import Depends
from typing import Annotated

from config.settings import get_settings
from usecases.user.usecase import (
    UserRepositoryInterface, 
    UserAddInteractor, UserAddInputBoundary, UserAddOutputBoundary,
    UserGetInteractor, UserGetInputBoundary, UserGetOutputBoundary,
    UserGetAllInteractor, UserGetAllInputBoundary, UserGetAllOutputBoundary
)
from infrastructure.database.user.repository import UserRepositoryImpl
from infrastructure.mock.user.repository import MockUserRepositoryImpl
from interfaces.presenters.user.http_response_presenter import (
    HttpResponseUserAddPresenter, 
    HttpResponseUserGetPresenter, 
    HttpResponseUserGetAllPresenter
)

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

def get_user_add_presenter() -> UserAddOutputBoundary:
    """ユーザー登録用プレゼンターを提供"""
    return HttpResponseUserAddPresenter()

def get_user_get_presenter() -> UserGetOutputBoundary:
    """ユーザー取得用プレゼンターを提供"""
    return HttpResponseUserGetPresenter()

def get_user_get_all_presenter() -> UserGetAllOutputBoundary:
    """全ユーザー取得用プレゼンターを提供"""
    return HttpResponseUserGetAllPresenter()

def get_user_add_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserAddOutputBoundary, Depends(get_user_add_presenter)]
) -> UserAddInputBoundary:
    """ユーザー登録用ユースケースを提供"""
    return UserAddInteractor(repo, presenter)

def get_user_get_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserGetOutputBoundary, Depends(get_user_get_presenter)]
) -> UserGetInputBoundary:
    """ユーザー取得用ユースケースを提供"""
    return UserGetInteractor(repo, presenter)

def get_user_get_all_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserGetAllOutputBoundary, Depends(get_user_get_all_presenter)]
) -> UserGetAllInputBoundary:
    """全ユーザー取得用ユースケースを提供"""
    return UserGetAllInteractor(repo, presenter) 