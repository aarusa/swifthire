from fastapi import APIRouter, HTTPException
import schemas
from data.users import userData

router = APIRouter()

# --------------- User Routes ------------------------
# Displaying user list
@router.get("/list")
def get_user_list():
    return userData

# Displaying single user based on id
@router.get("/{id}")
def get_user_by_id(id:int):
    return userData[id]

# Adding a new user
@router.post("/add")
async def add_user(new_user: schemas.User):
    # 1. Convert the incoming Pydantic model to a Python Dictionary
    user_dict = new_user.model_dump()
    
    # 2. Check if the user_id already exists to prevent duplicates
    if any(u['user_id'] == user_dict['user_id'] for u in userData):
        raise HTTPException(status_code=400, detail="User ID already exists")

    # 3. Add the dictionary to your list
    userData.append(user_dict)
    
    return {"message": "User added successfully", "data": user_dict}