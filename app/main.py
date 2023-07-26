# app/main.py
from fastapi import FastAPI
import aioredis
# from .routers import asset, user
from routers.asset import router as asset_router
from routers.user import router as user_router
app = FastAPI()

# Connect to Redis
async def connect_to_redis():
    return await aioredis.create_redis_pool("redis://localhost")

# Close the Redis connection on app shutdown
@app.on_event("startup")
async def startup_event():
    app.redis = await connect_to_redis()

@app.on_event("shutdown")
async def shutdown_event():
    app.redis.close()
    await app.redis.wait_closed()

# Include routers
app.include_router(asset, tags=["Asset"], prefix="/asset")
app.include_router(user, tags=["UserInfo"], prefix="/user")
