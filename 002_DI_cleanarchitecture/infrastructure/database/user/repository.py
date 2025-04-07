from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
import os

from entities.user.entity import User
from usecases.user.usecase import UserRepositoryInterface

Base = declarative_base()

class UserModel(Base):
    """ユーザーのDBモデル"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

class UserRepositoryImpl(UserRepositoryInterface):
    """実際のデータベースを使用するリポジトリ実装"""
    def __init__(self, db_path: Optional[str] = None, db_url: Optional[str] = None):
        """
        初期化
        Args:
            db_path: SQLiteのDBパス（オプション）
            db_url: 完全なDB URL（オプション）
        """
        if db_url:
            # 完全なDB URL（PostgreSQL、MySQLなど）
            print(f"Creating engine with URL: {db_url}")
            self.engine = create_engine(db_url)
        elif db_path:
            # SQLite用のパス
            sqlite_url = f"sqlite:///{db_path}"
            print(f"Creating engine with URL: {sqlite_url}")
            self.engine = create_engine(sqlite_url)
        else:
            # デフォルトはインメモリSQLite
            print("Creating in-memory SQLite engine")
            self.engine = create_engine("sqlite:///:memory:")
        
        # テーブル作成
        try:
            Base.metadata.create_all(self.engine)
            print("Database tables created successfully")
        except Exception as e:
            print(f"Error creating database tables: {e}")
            
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def create_user(self, user: User) -> User:
        """ユーザーを作成"""
        db = self.SessionLocal()
        try:
            db_user = UserModel(name=user.name, email=user.email)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            result = User(id=db_user.id, name=db_user.name, email=db_user.email)
            return result
        except Exception as e:
            db.rollback()
            print(f"Error creating user: {e}")
            raise
        finally:
            db.close()
    
    def get_user(self, user_id: int) -> User:
        """ユーザーを取得"""
        db = self.SessionLocal()
        try:
            db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
            if db_user is None:
                raise Exception("User not found")
            return User(id=db_user.id, name=db_user.name, email=db_user.email)
        finally:
            db.close()
    
    def get_all_users(self) -> List[User]:
        """すべてのユーザーを取得"""
        db = self.SessionLocal()
        try:
            db_users = db.query(UserModel).all()
            return [User(id=user.id, name=user.name, email=user.email) for user in db_users]
        finally:
            db.close()