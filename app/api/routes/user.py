from fastapi import APIRouter
from typing import Optional


router = APIRouter()

@router.get("")
async def get_users():
    return [{'user1':'content1'}, {'user2':'content2'}]

@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    return {'user_id':user_id}
