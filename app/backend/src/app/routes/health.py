from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db

router = APIRouter()

@router.get("/ping")
async def ping(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    return {"status": "ok", "message": "pong"}
