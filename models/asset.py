from pydantic import BaseModel
from typing import List

class AssetModel(BaseModel):
    movie_id: str
    comments: List[str]
    users: set
    user_who_commented: set

# models/user.py
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    user_id: str
    seller_info: bool
    buyer_info: bool