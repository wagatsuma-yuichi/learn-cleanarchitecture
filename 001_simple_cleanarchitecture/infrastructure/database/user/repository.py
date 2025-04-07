from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from entities.user.entity import User
from usecases.user.usecase import UserRepositoryInterface

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

class UserRepositoryImpl(UserRepositoryInterface):
    def __init__(self, db_path: str):
        engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def create_user(self, user: User) -> User:
        db = self.SessionLocal()
        db_user = UserModel(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        db.close()
        return User(id=db_user.id, name=db_user.name, email=db_user.email)

    def get_user(self, user_id: int) -> User:
        db = self.SessionLocal()
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        db.close()
        if db_user is None:
            raise Exception("User not found")
        return User(id=db_user.id, name=db_user.name, email=db_user.email)

    def get_all_users(self) -> list[User]:
        db = self.SessionLocal()
        db_users = db.query(UserModel).all()
        db.close()
        return [User(id=user.id, name=user.name, email=user.email) for user in db_users]