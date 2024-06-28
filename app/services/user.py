from sqlalchemy.orm import Session
from app.models.database import User
from app.core.security import get_password_hash, verify_password

class UserService:
    @staticmethod
    def create_user(db: Session, username: str, email: str, password: str):
        hashed_password = get_password_hash(password)
        db_user = User(username=username, email=email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if not user or not verify_password(password, user.hashed_password):
            return False
        return user