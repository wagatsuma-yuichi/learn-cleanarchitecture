from fastapi import status

from usecases.user.usecase import UserAddOutputBoundary, UserGetOutputBoundary, UserGetAllOutputBoundary
from usecases.user.data import UserAddOutputData, UserGetOutputData, UserGetAllOutputData, ErrorOutputData
from interfaces.views.view_models import (
    HttpResponseUserViewModel,
    HttpResponseUserListViewModel,
    HttpResponseErrorViewModel
)

class HttpResponseUserAddPresenter(UserAddOutputBoundary):
    """ユーザー登録結果をHTTPレスポンス用に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = HttpResponseUserViewModel()
    
    def output(self, output_data: UserAddOutputData) -> None:
        """ユーザー登録結果をビューモデルに変換"""
        self.view_model = HttpResponseUserViewModel(status.HTTP_201_CREATED)
        self.view_model.set_body(output_data.to_dict())
        self.view_model.add_header("Location", f"/users/{output_data.id}")
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = HttpResponseErrorViewModel(status.HTTP_400_BAD_REQUEST, output_data.message)
    
    def get_view_model(self) -> HttpResponseUserViewModel:
        """ビューモデルを取得"""
        return self.view_model

class HttpResponseUserGetPresenter(UserGetOutputBoundary):
    """ユーザー取得結果をHTTPレスポンス用に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = HttpResponseUserViewModel()
    
    def output(self, output_data: UserGetOutputData) -> None:
        """ユーザー取得結果をビューモデルに変換"""
        self.view_model = HttpResponseUserViewModel()
        self.view_model.set_body(output_data.to_dict())
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = HttpResponseErrorViewModel(status.HTTP_404_NOT_FOUND, output_data.message)
    
    def get_view_model(self) -> HttpResponseUserViewModel:
        """ビューモデルを取得"""
        return self.view_model

class HttpResponseUserGetAllPresenter(UserGetAllOutputBoundary):
    """全ユーザー取得結果をHTTPレスポンス用に変換するプレゼンター"""
    
    def __init__(self):
        self.view_model = HttpResponseUserListViewModel()
    
    def output(self, output_data: UserGetAllOutputData) -> None:
        """全ユーザー取得結果をビューモデルに変換"""
        self.view_model = HttpResponseUserListViewModel()
        self.view_model.set_body({"users": output_data.to_dict()["users"]})
    
    def output_error(self, output_data: ErrorOutputData) -> None:
        """エラー情報をビューモデルに変換"""
        self.view_model = HttpResponseErrorViewModel(status.HTTP_500_INTERNAL_SERVER_ERROR, output_data.message)
    
    def get_view_model(self) -> HttpResponseUserListViewModel:
        """ビューモデルを取得"""
        return self.view_model 