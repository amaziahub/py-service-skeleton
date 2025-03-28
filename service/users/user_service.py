from sqlalchemy.orm import Session

from service.users.models.user import UserDB
from service.users.scemas.user import UserCreate
from service.users.utils import hash_password


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate) -> UserDB:
        hashed_pw = hash_password(user_data.password)
        user = UserDB(username=user_data.username, password=hashed_pw)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str):
        return self.db.query(UserDB).filter(UserDB.username == username).first()
