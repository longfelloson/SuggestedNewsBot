from sqlalchemy import Column, String, Integer

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    is_blocked = Column(String, default=False)
