from pydantic import BaseModel

class User(BaseModel):
    """ユーザーエンティティ"""
    id: int = 0
    name: str
    email: str