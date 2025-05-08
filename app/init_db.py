import asyncio
from database import engine, Base

async def init_models():
    async with engine.begin() as conn:
        print("Creating tables...")
        # await conn.run_sync(Base.metadata.drop_all)  # Optional: Wipe existing data
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_models())
