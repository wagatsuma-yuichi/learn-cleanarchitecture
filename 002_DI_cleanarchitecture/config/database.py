from infrastructure.database.user.repository import UserRepositoryImpl
from infrastructure.mock.user.repository import MockUserRepositoryImpl
from usecases.user.usecase import UserRepositoryInterface
from config.environment import env

def get_repository(db_url: str | None = None) -> UserRepositoryInterface:
    """リポジトリのインスタンスを取得する

    Args:
        db_url (str | None, optional): データベースURL. Defaults to None.

    Returns:
        UserRepository: リポジトリのインスタンス
    """
    if db_url is None:
        db_url = env.DATABASE_URL

    if db_url is None:
        # モックリポジトリを使用
        print(f"Using mock repository for environment: {env.APP_ENV}")
        return MockUserRepositoryImpl()

    # PostgreSQLに接続
    print(f"Connecting to PostgreSQL database at {db_url}")
    return UserRepositoryImpl(db_url=db_url)