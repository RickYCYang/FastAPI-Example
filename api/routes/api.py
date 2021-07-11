from fastapi import APIRouter

from api.routes import item
from api.routes import user

router = APIRouter()
# example router
router.include_router(item.router, tags=["example"], prefix="/items")
router.include_router(user.router, tags=["example2"], prefix="/users")
