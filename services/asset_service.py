from cassandra.cqlengine.models import Model
from ..database import get_session
from ..models.asset import AssetModel

class AssetService:
    @classmethod
    async def create_asset(cls, asset_data: AssetModel):
        session = get_session()
        asset = Model(**asset_data.dict())
        return asset.save()

    @classmethod
    async def get_all_assets(cls):
        session = get_session()
        return list(Model.objects.all())

    @classmethod
    async def get_asset_by_id(cls, id: str):
        session = get_session()
        return list(Model.objects.filter(movie_id=id))