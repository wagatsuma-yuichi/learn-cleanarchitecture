from pydantic import BaseModel, Field, EmailStr, validator

class User(BaseModel):
    """ユーザーエンティティ"""
    id: int = Field(gt=0, default=0, description="ユーザーID")
    name: str = Field(min_length=1, max_length=100, description="ユーザー名")
    email: EmailStr

    # カスタム検証: 特定のドメインのみ許可する例
    @validator('email')
    def validate_email_domain(cls, v):
        # 許可するドメインのリスト
        allowed_domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
        domain = v.split('@')[-1]
        if domain not in allowed_domains:
            raise ValueError(f"メールドメインは次のいずれかである必要があります: {', '.join(allowed_domains)}")
        return v
        
    class Config:
        # Pydantic 1.xのvalidatorで必要なフィールド検証設定
        validate_assignment = True