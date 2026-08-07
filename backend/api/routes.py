from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["CURE Protocol"],
)


@router.get("/")
def api_root():
    return {
        "message": "CURE Protocol API v1"
    }


@router.get("/health")
def health():
    return {
        "status": "ok"
    }
