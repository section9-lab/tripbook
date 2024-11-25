import os
import uvicorn

from fastapi import FastAPI
from dotenv import load_dotenv

from contextlib import asynccontextmanager
from app.api.routes import router
from app.db.models import Base
from app.db.database import engine


# 初始化数据库表
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="Travel Planner API")

# 应用启动时创建表
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
