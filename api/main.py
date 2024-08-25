from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestModel(BaseModel):
    full_name: str
    dob: str 
    numbers: List[int]
    alphabets: List[str]


def get_highest_lowercase(alphabets: List[str]) -> List[str]:
    lowercase = [ch for ch in alphabets if ch.islower()]
    return [max(lowercase)] if lowercase else []

def get_number_list(data):
    l = []
    for i in data:
        if i.isnumeric():
            l.append(i)
    return l

def get_alphabet_list(data):
    l = []
    for i in data:
        if i.isnumeric():
            l.append(i)
    return l


@app.post("/bfhl/")
async def process_bfhl(data: RequestModel):
    try:
        highest_lowercase = get_highest_lowercase(data.alphabets)
        get_number = get_number_list(data);
        get_alphabet=get_alphabet_list(data);
        
        return {
            "user_id": "Karthik_r_06042003",
            "is_success": True,
            "numbers": get_number,
            "alphabets": get_alphabet,
            "highest_lowercase_alphabet": highest_lowercase,
            "email": "karthik.r2021b@vitstudent.ac.in",
            "roll_number": "21BCE5481"
        }
    except Exception as e:
        return {
            "user_id": None,
            "is_success": False,
            "message": str(e),
            "email": "karthik.r2021b@vitstudent.ac.in",
            "roll_number": "21BCE5481"
        }


@app.get("/bfhl/")
async def get_bfhl_operation_code():
    return {"operation_code": 1}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
