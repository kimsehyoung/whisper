from fastapi import APIRouter

router = APIRouter()

@router.get("", tags=["health"], summary="Health check")
def health_check():
    return {"status": "ok"}