from fastapi.responses import JSONResponse
from typing import Dict, Any, List

from interfaces.views.view_models import (
    HttpResponseViewModel,
    HttpResponseUserListViewModel,
    HttpResponseErrorViewModel,
)

class HttpResponseView:
    """HTTP応答を生成するビュー"""
    
    @staticmethod
    def render(view_model: HttpResponseViewModel) -> JSONResponse:
        """ビューモデルからHTTPレスポンスを生成"""
        return JSONResponse(
            content=view_model.get_body(),
            status_code=view_model.get_status_code(),
            headers=view_model.get_headers()
        )
    
    @staticmethod
    def render_json(view_model: HttpResponseViewModel) -> Dict[str, Any]:
        """ビューモデルからJSONデータを生成"""
        return view_model.get_body()
    
    @staticmethod
    def render_users_json(view_model: HttpResponseUserListViewModel) -> List[Dict[str, Any]]:
        """ユーザーリストビューモデルからJSONデータを生成"""
        return view_model.get_users()

    @staticmethod
    def render_error(view_model: HttpResponseViewModel) -> JSONResponse:
        """エラービューモデルからHTTPレスポンスを生成"""
        body = view_model.get_body()
        return JSONResponse(
            content=body,
            status_code=view_model.get_status_code()
        )
