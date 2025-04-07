import os
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """アプリケーション設定"""
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DATABASE_URL: str = "sqlite:///./default.db"
    
    @property
    def USE_MOCK_DB(self) -> bool:
        """環境に応じてモックDBを使用するかどうかを決定
        development: モックDBを使用
        test: 実際のDBを使用（テスト用）
        production: 実際のDBを使用
        """
        return self.APP_ENV.lower() == "development"
    
    class Config:
        env_file = f".env.{os.getenv('APP_ENV', 'development')}.local"
        extra = "ignore"  # 追加のフィールドは無視

@lru_cache()
def get_settings():
    """キャッシュされた設定を取得"""
    return Settings() 