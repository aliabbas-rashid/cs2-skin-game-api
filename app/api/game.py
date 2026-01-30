from fastapi import APIRouter

router = APIRouter()

@router.get("/state")
def get_state():
    return {
        "game_id": 123,
        "remainingTime": 60,
        "score": 0,
        "skin": {
            "id": 1,
            "url": ""
        }
    }