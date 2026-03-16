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

# --------------- Candidate Model ------------------------
class CandidateProfile(BaseModel):
    name: str
    email: str
    skills: List[str]
    experience_summary: str
    years_of_experience: int

# --------------- Job Description Model ------------------------
class JobDescription(BaseModel):
    title: str
    company: str
    required_skills: List[str]
    min_years_experience: int
    description_text: str