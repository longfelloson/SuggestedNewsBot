from pydantic import BaseModel


class NewsSchema(BaseModel):
    id_: int
    from_user_id: int
    from_channel_id: int
    from_channel_message_id: int
    chat_message_id: int
