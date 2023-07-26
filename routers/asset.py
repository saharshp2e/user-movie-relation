from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models.asset import AssetModel
from models.schema import ResponseModel, ErrorResponseModel
from services.asset_service import AssetService

router = APIRouter()

@router.post("/", response_description="Asset data added into the database")
async def add_asset_data(asset: AssetModel = Body(...)):
    asset_data = jsonable_encoder(asset)
    new_asset = await AssetService.create_asset(asset_data)
    return ResponseModel(new_asset, "Asset added successfully.")

@router.get("/", response_description="Assets retrieved")
async def get_assets():
    assets = await AssetService.get_all_assets()
    if assets:
        return ResponseModel(assets, "Assets data retrieved successfully")
    return ResponseModel(assets, "Empty list returned")

@router.get("/{id}", response_description="Asset data retrieved")
async def get_asset_data(id: str):
    asset = await AssetService.get_asset_by_id(id)
    if asset:
        return ResponseModel(asset, "Asset data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Asset doesn't exist.")