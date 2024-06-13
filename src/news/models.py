from sqlalchemy import Column, Integer

from src.database import Base


class News(Base):
    __tablename__ = 'news'

    id_ = Column(Integer, primary_key=True, autoincrement=False)
    from_user_id = Column(Integer)
    from_channel_id = Column(Integer)
    from_channel_message_id = Column(Integer)
    chat_message_id = Column(Integer)
