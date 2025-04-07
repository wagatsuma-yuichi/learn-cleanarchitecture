from functools import lru_cache
import os

from pydantic_settings import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("APP_ENV")
    return f".env.{runtime_env}.local" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    APP_ENV: str = "development"
    DATABASE_DIALECT: str | None = None
    DATABASE_HOSTNAME: str | None = None
    DATABASE_NAME: str | None = None
    DATABASE_PASSWORD: str | None = None
    DATABASE_PORT: int | None = None
    DATABASE_USERNAME: str | None = None
    DEBUG_MODE: bool

    # データベースURL（計算プロパティ）
    @property
    def DATABASE_URL(self) -> str | None:
        if self.USE_MOCK_DB:
            return None
        if not all([
            self.DATABASE_DIALECT,
            self.DATABASE_USERNAME,
            self.DATABASE_PASSWORD,
            self.DATABASE_HOSTNAME,
            self.DATABASE_PORT,
            self.DATABASE_NAME
        ]):
            return None
        # PostgreSQLのURL形式のみをサポート
        return f"postgresql://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOSTNAME}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
    
    # 環境に応じてモックDBを使用するかどうかを決定
    @property
    def USE_MOCK_DB(self) -> bool:
        return self.APP_ENV.lower() in ["development", "develop"]

    model_config = {
        "env_file": get_env_filename(),
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "env_prefix": "",
        "extra": "allow"
    }


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()


# シングルトンとしてのインスタンス
env = get_environment_variables() 