from typing import Dict, List, Any
from entities.user.entity import User
from usecases.user.usecase import UserOutputBoundary

class UserViewModel:
    """ユーザー表示用のビューモデル"""
    def __init__(self, id: int, name: str, email: str, display_name: str = None):
        self.id = id
        self.name = name
        self.email = email
        self.display_name = display_name or name
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "display_name": self.display_name
        }

class UserPresenter(UserOutputBoundary):
    """ユーザー情報の表示形式を変換するプレゼンター"""
    
    def present_user(self, user: User) -> Dict[str, Any]:
        """ユーザー情報をビューモデルに変換"""
        view_model = UserViewModel(
            id=user.id,
            name=user.name,
            email=user.email,
            display_name=f"{user.name}さん"  # 日本語表示用に加工
        )
        return view_model.to_dict()
    
    def present_users(self, users: List[User]) -> List[Dict[str, Any]]:
        """ユーザーリストをビューモデルリストに変換"""
        return [self.present_user(user) for user in users]
    
    def present_error(self, message: str) -> Dict[str, Any]:
        """エラー情報をビューモデルに変換"""
        return {
            "error": True,
            "message": message
        } 