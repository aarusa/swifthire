from pydantic import BaseModel
from typing import List

# class Item(BaseModel):
#     task: str

# --------------- User Model ------------------------
class User(BaseModel):
    user_id: int
    username: str
    first_name: str
    last_name: str
    email: str
    location: str
    account_tier: str = "Free"
    is_active: bool = True

# --------------- Resume Model ------------------------
class Resume(BaseModel):
    resume_id: int
    user_id: int
    first_name: str
    last_name: str
    job_title: str
    years_experience: int
    skills: List[str] # Validates that this is a list of strings
    education: str

