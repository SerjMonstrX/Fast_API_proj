from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.dao import BookingDao
from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)

@router.get("")
async def get_bookings():
    return await BookingDao.find_all()

