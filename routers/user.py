from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from ..models.user import UserRequestModel
from ..models.schema import ResponseModel, ErrorResponseModel
from ..services.user_service import UserService

router = APIRouter()

@router.post("/info", response_description="serves user info based on request")
async def get_temporal_user_features(user_request: UserRequestModel = Body(...)):
    # Implement user-related logic here...
    pass