from sqlalchemy import Column, Integer, String, JSON
from pydantic import BaseModel
from typing import List
from .database import Base

# --- DATABASE MODELS (Table for Jobs) ---

class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    required_skills = Column(JSON) # SQLite can store lists as JSON!
    min_years_experience = Column(Integer)
    description_text = Column(String)


# --- API SCHEMAS (Pydantic Molds for JSON) ---
class CandidateProfile(BaseModel):
    name: str
    email: str
    skills: List[str]
    experience_summary: str
    years_of_experience: int

class MatchResult(BaseModel):
    match_score: int
    fit_summary: str
    missing_skills: List[str]