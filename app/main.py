from fastapi import FastAPI
from app.api.routes import router
from app.db.models import Base
from app.db.database import engine

# 初始化数据库表
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="Travel Planner API")

@app.on_event("startup")
async def on_startup():
    await init_db()


if __name__ == "__main__":
    app.include_router(router)
