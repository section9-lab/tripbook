from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Trip
from app.db.schemas import TripCreate

async def create_trip(db: AsyncSession, trip: TripCreate) -> Trip:
    new_trip = Trip(destination=trip.destination, start_date=trip.start_date, end_date=trip.end_date)
    db.add(new_trip)
    await db.commit()
    await db.refresh(new_trip)
    return new_trip

async def get_trip(db: AsyncSession, trip_id: int) -> Trip:
    result = await db.execute(select(Trip).where(Trip.id == trip_id))
    return result.scalars().first()

async def get_all_trips(db: AsyncSession) -> list[Trip]:
    result = await db.execute(select(Trip))
    return result.scalars().all()

async def update_trip(db: AsyncSession, trip_id: int, trip: TripCreate) -> Trip:
    existing_trip = await get_trip(db, trip_id)
    if existing_trip:
        existing_trip.destination = trip.destination
        existing_trip.start_date = trip.start_date
        existing_trip.end_date = trip.end_date
        await db.commit()
        await db.refresh(existing_trip)
    return existing_trip

async def delete_trip(db: AsyncSession, trip_id: int) -> bool:
    trip = await get_trip(db, trip_id)
    if trip:
        await db.delete(trip)
        await db.commit()
        return True
    return False
