from fastapi import APIRouter, Depends, HTTPException
from app.auth import get_current_user
from app.utils import search_flights

router = APIRouter()

@router.post("/search")
async def search_multi_city(request: dict, user=Depends(get_current_user)):
    if not user.get("is_paid"):
        raise HTTPException(status_code=402, detail="Subscription required")
    try:
        return await search_flights(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
