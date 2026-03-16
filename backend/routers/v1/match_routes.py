import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from google import genai
from .database import get_db
from .models import JobModel, CandidateProfile, MatchResult

router = APIRouter()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@router.post("/score/{job_id}")
async def score_candidate(
    job_id: int, 
    candidate: CandidateProfile, 
    db: Session = Depends(get_db)
):
    # 1. Get the Job from the real Database
    job = db.query(JobModel).filter(JobModel.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found in database")

    # 2. Build the Recruiter Prompt
    prompt = f"""
    You are a Senior Technical Recruiter. Compare the candidate to the job requirements.
    
    JOB REQUIREMENTS:
    - Role: {job.title}
    - Company: {job.company}
    - Required Skills: {", ".join(job.required_skills)}
    - Experience Needed: {job.min_years_experience} years
    
    CANDIDATE DATA:
    - Name: {candidate.name}
    - Skills: {", ".join(candidate.skills)}
    - Experience: {candidate.years_of_experience} years
    - Professional Summary: {candidate.experience_summary}
    
    Provide a match score (0-100), a detailed fit summary, and a list of missing skills.
    """

    # 3. Request Structured Output from Gemini
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": MatchResult,
            }
        )
        return {"status": "success", "match": response.parsed}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Matching failed: {str(e)}")