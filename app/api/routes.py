from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.schemas import TripCreate, TripResponse
from app.service.tripservice import create_trip, get_trip, get_all_trips, update_trip, delete_trip

router = APIRouter()

@router.get("/")
def read_root():
    return "Welcome to Travel Planner API!"


@router.post("/trips", response_model=TripResponse)
async def api_create_trip(trip: TripCreate, db: AsyncSession = Depends(get_db)):
    return await create_trip(db, trip)

@router.get("/trips/{trip_id}", response_model=TripResponse)
async def api_get_trip(trip_id: int, db: AsyncSession = Depends(get_db)):
    trip = await get_trip(db, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.get("/trips", response_model=list[TripResponse])
async def api_get_all_trips(db: AsyncSession = Depends(get_db)):
    return await get_all_trips(db)

@router.put("/trips/{trip_id}", response_model=TripResponse)
async def api_update_trip(trip_id: int, trip: TripCreate, db: AsyncSession = Depends(get_db)):
    updated_trip = await update_trip(db, trip_id, trip)
    if not updated_trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return updated_trip

@router.delete("/trips/{trip_id}")
async def api_delete_trip(trip_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_trip(db, trip_id)
    if not success:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": f"Trip with ID {trip_id} has been deleted."}
