# models/user.py
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    user_id: str
    seller_info: bool
    buyer_info: bool