from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Administration"])


class Health(BaseModel):
    healthy: bool


@router.get(
    "/health",
    operation_id="getHealth",
    response_model=Health,
)
def get_health_status():
    """Returns health status"""
    return Health(healthy=True)