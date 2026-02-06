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

@router.post("/guess")
def submit_guess(payload: dict):
    return {
        "correct": False,
        "message": "Incorrect, try again"
    }

@router.post("/start")
def start_game(payload: dict):
    return {
        "game_id": "demo",
        "timeLimit": 60
    }