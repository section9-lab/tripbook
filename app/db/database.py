import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

# 将 'postgres://' 替换为 'postgresql+asyncpg://'
DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://")

print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session
