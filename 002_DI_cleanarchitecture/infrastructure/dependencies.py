from fastapi import Depends
from typing import Annotated

from config.database import get_repository
from usecases.user.usecase import (
    UserRepositoryInterface, 
    UserAddInteractor, UserAddInputBoundary, UserAddOutputBoundary,
    UserGetInteractor, UserGetInputBoundary, UserGetOutputBoundary,
    UserGetAllInteractor, UserGetAllInputBoundary, UserGetAllOutputBoundary,
    UserDeleteInteractor, UserDeleteInputBoundary, UserDeleteOutputBoundary
)
from interfaces.presenters.user.http_response_presenter import (
    HttpResponseUserAddPresenter, 
    HttpResponseUserGetPresenter, 
    HttpResponseUserGetAllPresenter,
    HttpResponseUserDeletePresenter
)



def get_user_add_presenter() -> UserAddOutputBoundary:
    """ユーザー登録用プレゼンターを提供"""
    return HttpResponseUserAddPresenter()

def get_user_get_presenter() -> UserGetOutputBoundary:
    """ユーザー取得用プレゼンターを提供"""
    return HttpResponseUserGetPresenter()

def get_user_get_all_presenter() -> UserGetAllOutputBoundary:
    """全ユーザー取得用プレゼンターを提供"""
    return HttpResponseUserGetAllPresenter()

def get_user_delete_presenter() -> UserDeleteOutputBoundary:
    """ユーザー削除用プレゼンターを提供"""
    return HttpResponseUserDeletePresenter()

def get_user_add_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserAddOutputBoundary, Depends(get_user_add_presenter)]
) -> UserAddInputBoundary:
    """ユーザー登録用ユースケースを提供"""
    return UserAddInteractor(repo, presenter)

def get_user_get_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserGetOutputBoundary, Depends(get_user_get_presenter)]
) -> UserGetInputBoundary:
    """ユーザー取得用ユースケースを提供"""
    return UserGetInteractor(repo, presenter)

def get_user_get_all_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserGetAllOutputBoundary, Depends(get_user_get_all_presenter)]
) -> UserGetAllInputBoundary:
    """全ユーザー取得用ユースケースを提供"""
    return UserGetAllInteractor(repo, presenter) 

def get_user_delete_usecase(
    repo: Annotated[UserRepositoryInterface, Depends(get_repository)],
    presenter: Annotated[UserDeleteOutputBoundary, Depends(get_user_delete_presenter)]
) -> UserDeleteInputBoundary:
    """ユーザー削除用ユースケースを提供"""
    return UserDeleteInteractor(repo, presenter)