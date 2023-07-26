from pydantic import BaseModel

class ResponseModel(BaseModel):
    data: list
    code: int
    message: str

class ErrorResponseModel(BaseModel):
    error: str
    code: int
    message: str