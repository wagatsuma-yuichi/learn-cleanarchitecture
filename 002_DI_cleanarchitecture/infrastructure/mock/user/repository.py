from typing import List, Dict

from entities.user.entity import User
from usecases.user.usecase import UserRepositoryInterface

class MockUserRepositoryImpl(UserRepositoryInterface):
    """モックデータを使用するリポジトリ実装"""
    def __init__(self):
        # インメモリデータストア
        self.users: Dict[int, User] = {}
        self.counter = 1
        
        # テスト用の初期データをロード
        self._load_initial_data()
    
    def _load_initial_data(self):
        """テスト用の初期データをロード"""
        test_users = [
            User(id=1, name="テストユーザー1", email="user1@example.com"),
            User(id=2, name="テストユーザー2", email="user2@example.com"),
        ]
        for user in test_users:
            self.users[user.id] = user
            if user.id >= self.counter:
                self.counter = user.id + 1
    
    def create_user(self, user: User) -> User:
        """ユーザーを作成"""
        user_id = self.counter
        self.counter += 1
        new_user = User(id=user_id, name=user.name, email=user.email)
        self.users[user_id] = new_user
        return new_user
    
    def get_user(self, user_id: int) -> User:
        """ユーザーを取得"""
        if user_id not in self.users:
            raise Exception("User not found")
        return self.users[user_id]
    
    def get_all_users(self) -> List[User]:
        """すべてのユーザーを取得"""
        return list(self.users.values()) 