from typing import Dict, Any, Optional, List
from fastapi import status

class HttpResponseViewModel:
    """HTTP応答用のビューモデルの基底クラス"""
    
    def __init__(self, status_code: int = status.HTTP_200_OK):
        self.status_code = status_code
        self.headers: Dict[str, str] = {}
        self.body: Dict[str, Any] = {}
    
    def add_header(self, name: str, value: str) -> None:
        """ヘッダーを追加"""
        self.headers[name] = value
    
    def set_body(self, body: Dict[str, Any]) -> None:
        """ボディを設定"""
        self.body = body
    
    def get_status_code(self) -> int:
        """ステータスコードを取得"""
        return self.status_code
    
    def get_headers(self) -> Dict[str, str]:
        """ヘッダーを取得"""
        return self.headers
    
    def get_body(self) -> Dict[str, Any]:
        """ボディを取得"""
        return self.body

class HttpResponseUserViewModel(HttpResponseViewModel):
    """ユーザー情報を含むHTTP応答用ビューモデル"""
    
    def __init__(self, status_code: int = status.HTTP_200_OK):
        super().__init__(status_code)

class HttpResponseUserListViewModel(HttpResponseViewModel):
    """ユーザーリストを含むHTTP応答用ビューモデル"""
    
    def __init__(self, status_code: int = status.HTTP_200_OK):
        super().__init__(status_code)
        self.body = {"users": []}
    
    def get_users(self) -> List[Dict[str, Any]]:
        """ユーザーリストを取得"""
        return self.body["users"]

class HttpResponseErrorViewModel(HttpResponseViewModel):
    """エラー情報を含むHTTP応答用ビューモデル"""
    
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST, message: str = ""):
        super().__init__(status_code)
        self.body = {"error": True, "message": message} 