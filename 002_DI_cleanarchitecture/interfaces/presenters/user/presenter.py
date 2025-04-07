from typing import Dict, List, Any
from entities.user.entity import User
from usecases.user.usecase import UserAddOutputBoundary, UserGetOutputBoundary, UserGetAllOutputBoundary
from usecases.user.data import (
    UserAddOutputData, UserGetOutputData, 
    UserGetAllOutputData, ErrorOutputData
)

class UserViewModel:
    """表示用のビューモデルの基底クラス"""
    def __init__(self):
        self.data = {}
        
    def to_dict(self) -> Dict[str, Any]:
        return self.data
        
class UserAddViewModel(UserViewModel):
    """ユーザー登録結果の表示用モデル"""
    def __init__(self):
        super().__init__()
        self.data = {}
        
class UserGetViewModel(UserViewModel):
    """ユーザー取得結果の表示用モデル"""
    def __init__(self):
        super().__init__()
        self.data = {}
        
class UserGetAllViewModel(UserViewModel):
    """全ユーザー取得結果の表示用モデル"""
    def __init__(self):
        super().__init__()
        self.data = {"users": []}
        
class ErrorViewModel(UserViewModel):
    """エラー表示用モデル"""
    def __init__(self):
        super().__init__()
        self.data = {"error": True, "message": ""}

class UserAddPresenter(UserAddOutputBoundary):
    """ユーザー登録結果を表示形式に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = UserAddViewModel()
    
    def output(self, output_data: UserAddOutputData) -> None:
        """登録結果をビューモデルに変換"""
        self.view_model.data = output_data.to_dict()
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = ErrorViewModel()
        self.view_model.data = output_data.to_dict()
        
    def get_view_model(self) -> Dict[str, Any]:
        """ビューモデルを取得"""
        return self.view_model.to_dict()

class UserGetPresenter(UserGetOutputBoundary):
    """ユーザー取得結果を表示形式に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = UserGetViewModel()
    
    def output(self, output_data: UserGetOutputData) -> None:
        """取得結果をビューモデルに変換"""
        self.view_model.data = output_data.to_dict()
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = ErrorViewModel()
        self.view_model.data = output_data.to_dict()
        
    def get_view_model(self) -> Dict[str, Any]:
        """ビューモデルを取得"""
        return self.view_model.to_dict()

class UserGetAllPresenter(UserGetAllOutputBoundary):
    """全ユーザー取得結果を表示形式に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = UserGetAllViewModel()
    
    def output(self, output_data: UserGetAllOutputData) -> None:
        """取得結果をビューモデルに変換"""
        self.view_model.data = {"users": output_data.to_dict()["users"]}
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = ErrorViewModel()
        self.view_model.data = output_data.to_dict()
        
    def get_view_model(self) -> List[Dict[str, Any]]:
        """ビューモデルを取得"""
        return self.view_model.to_dict()["users"] 