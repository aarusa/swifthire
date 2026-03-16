from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db, engine
from .models import JobModel, Base
from pydantic import BaseModel
from typing import List

# This line creates the actual database table if it doesn't exist
Base.metadata.create_all(bind=engine)

router = APIRouter()

# Schema for incoming data (Pydantic)
class JobCreate(BaseModel):
    title: str
    company: str
    required_skills: List[str]
    min_years_experience: int
    description_text: str

@router.post("/create")
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = JobModel(
        title=job.title,
        company=job.company,
        required_skills=job.required_skills,
        min_years_experience=job.min_years_experience,
        description_text=job.description_text
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return {"status": "success", "job_id": new_job.id}

@router.get("/list")
async def list_jobs(db: Session = Depends(get_db)):
    jobs = db.query(JobModel).all()
    return {"jobs": jobs}