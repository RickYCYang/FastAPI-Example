from fastapi import APIRouter
from typing import Optional


router = APIRouter()

@router.get("")
async def get_items():
    return [{'foo':'bar'}, {'foo2':'bar2'}]


@router.get("/{id}")
async def get_item_by_id(id: int, q: Optional[int] = None):
    return {"id": id, "q": q}