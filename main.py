from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI()

class PostRequest(BaseModel):
    data: List[str]

class PostResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_alphabet: List[str]

@app.post("/bfhl", response_model=PostResponse)
def process_data(request: PostRequest):
    try:
        numbers = [item for item in request.data if item.isdigit()]
        alphabets = [item for item in request.data if item.isalpha()]
        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []
        
        user_id = f"john_doe_{datetime.datetime.now().strftime('%d%m%Y')}"
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}
