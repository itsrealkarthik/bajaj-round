from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RequestModel(BaseModel):
    full_name: str
    dob: str 
    numbers: List[int]
    alphabets: List[str]


def get_highest_lowercase(alphabets: List[str]) -> List[str]:
    lowercase = [ch for ch in alphabets if ch.islower()]
    return [max(lowercase)] if lowercase else []


@app.post("/bfhl/")
async def process_bfhl(data: RequestModel):
    try:
        
        user_id = f"{data.full_name.lower().replace(' ', '_')}_{data.dob}"
        highest_lowercase = get_highest_lowercase(data.alphabets)
        
        return {
            "user_id": user_id,
            "is_success": True,
            "numbers": data.numbers,
            "alphabets": data.alphabets,
            "highest_lowercase": highest_lowercase
        }
    except Exception as e:
        return {
            "user_id": None,
            "is_success": False,
            "message": str(e)
        }


@app.get("/bfhl/")
async def get_bfhl_operation_code():
    return {"operation_code": 1}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
