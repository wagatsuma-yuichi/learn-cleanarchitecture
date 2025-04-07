from typing import Dict, Any, List
from usecases.interfaces import InputData, OutputData
from entities.user.entity import User

class UserAddInputData(InputData['UserAddOutputData']):
    """ユーザー登録用の入力データ"""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class UserAddOutputData(OutputData):
    """ユーザー登録用の出力データ"""
    def __init__(self, user: User):
        self.id = user.id
        self.name = user.name
        self.email = user.email
        self.display_name = f"{user.name}さん"  # 日本語表示用に加工
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "display_name": self.display_name
        }

class UserGetInputData(InputData['UserGetOutputData']):
    """ユーザー取得用の入力データ"""
    def __init__(self, user_id: int):
        self.user_id = user_id

class UserGetOutputData(OutputData):
    """ユーザー取得用の出力データ"""
    def __init__(self, user: User):
        self.id = user.id
        self.name = user.name
        self.email = user.email
        self.display_name = f"{user.name}さん"  # 日本語表示用に加工
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "display_name": self.display_name
        }

class UserGetAllInputData(InputData['UserGetAllOutputData']):
    """全ユーザー取得用の入力データ"""
    pass

class UserGetAllOutputData(OutputData):
    """全ユーザー取得用の出力データ"""
    def __init__(self, users: List[User]):
        self.users = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "display_name": f"{user.name}さん"
            }
            for user in users
        ]
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {"users": self.users}

class UserDeleteInputData(InputData['UserDeleteOutputData']):
    """ユーザー削除用の入力データ"""
    def __init__(self, user_id: int):
        self.user_id = user_id

class UserDeleteOutputData(OutputData):
    """ユーザー削除用の出力データ"""
    pass

class ErrorOutputData(OutputData):
    """エラー用の出力データ"""
    def __init__(self, message: str):
        self.error = True
        self.message = message
    
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "error": self.error,
            "message": self.message
        } 